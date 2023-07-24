import ast
import json
import random
from copy import deepcopy as copy
from inspect import getfullargspec, signature
from pathlib import Path
from typing import Any, Dict, List, Optional, Set, Type, Union, cast

from py2ai import components, enums
from py2ai.aia import Screen
from py2ai.blockly import Block, BlocklyProject
from py2ai.calls import ATTR_CALLS, CALLS, METHODS
from py2ai.components import Component, Form
from py2ai.const import VERSIONS

LIB = Path(__file__).parent / 'lib.xml'
ADD_COMPONENTS = [
    {'$Name': '__py2ai__notifier__', '$Type': 'Notifier', '$Version': '6', 'Uuid': '1'},
    {'$Name': '__py2ai__json__', '$Type': 'Web', '$Version': '8', 'Uuid': '2'},
]


def SCHEMA(name: str, appname: Optional[str] = None):
    return {
        'authURL': ['ai2.appinventor.mit.edu'],
        'YaVersion': '223',
        'Source': 'Form',
        'Properties': {
            '$Name': name,
            '$Type': 'Form',
            '$Version': '30',
            'AppName': appname or name,
            'Title': name,
            'Uuid': '0',
        },
    }


def _find_comp(root: dict, name: str) -> Optional[dict]:
    if root.get('$Name') == name:
        return root
    for comp in root.get('$Components', []):
        found = _find_comp(comp, name)
        if found:
            return found


def parse_args(names: List[str], args: list, kwargs: dict):
    parsed = {names[i]: args[i] for i in range(len(args))}
    for k, v in kwargs.items():
        if k in parsed:
            raise ValueError(f'Argument {k} specified twice')
        if k not in names:
            raise ValueError(f'Unknown argument {k}')
        parsed[k] = v
    return parsed


class NotSupportedError(Exception):
    pass


class ForceLocal:
    def __init__(self, compiler: 'PythonCompiler', *names: str):
        self.compiler = compiler
        self.names = names

    def __enter__(self):
        self.compiler._locals.update(self.names)

    def __exit__(self, *args):
        self.compiler._locals.difference_update(self.names)


class PythonCompiler(ast.NodeVisitor):
    def __init__(self) -> None:
        super().__init__()
        self.project = BlocklyProject()
        self._orig_schema = None
        self._schema = None
        self._state: List[ast.AST] = []
        self._scopes: List[Set[str]] = []
        self._comps: List[Dict[str, Type[Component]]] = []
        self._annots: List[Dict[str, type]] = []
        self._procs: Dict[str, List[str]] = {}
        self._globals: List[Set[str]] = []
        self._locals: Set[str] = set()
        self._ctx: dict = {}
        self._global_assigns: Dict[str, Block] = {}

    @property
    def _global(self):
        return len(self._scopes) <= 1

    def _local(self, *names: str):
        return ForceLocal(self, *names)

    def visit(self, node):
        self._state.append(node)
        ret = super().visit(node)
        self._state.pop()
        return ret

    def visit_nodes(self, nodes: list):
        blocks = []
        for item in nodes:
            blk = self.visit(item)
            # print(blk)
            if blk is not None:
                blocks.append(blk)
        if not blocks:
            return
        if blocks:
            first = blocks[0]
            cur = first
            for blk in blocks[1:]:
                while cur.next is not None:
                    cur = cur.next
                cur.next = blk
                cur = blk
            return first

    def generic_visit(self, node):
        raise NotSupportedError(f'{node.__class__.__name__} is not implemented')

    def _get_var_block(
        self, name: str, force_global: Optional[bool] = None, eventparam: bool = False
    ):
        if force_global is None:
            force_global = self._global and name not in self._locals
        return Block(
            'lexical_variable_get',
            fields={'VAR': ('global ' if force_global else '') + name},
            mutation_eventparams=[name] if eventparam else None,
        )

    def _set_var_block(
        self, name: str, value: Block, force_global: Optional[bool] = None
    ):
        if force_global is None:
            force_global = self._global and name not in self._locals
        return Block(
            'lexical_variable_set',
            fields={'VAR': ('global ' if force_global else '') + name},
            values={'VALUE': value},
        )

    def _get_null_block(self):
        return self._get_var_block('__py2ai__null__', True)

    def _get_proc_block(self, proc: str, args: List[str], values: List[Block]):
        return Block(
            'procedures_callreturn',
            mutations={'name': proc},
            mutation_args=args,
            fields={'PROCNAME': proc},
            values={f'ARG{i}': a for i, a in enumerate(values)},
        )

    def _get_annot(self, var: str):
        for i in range(len(self._scopes) - 1, -1, -1):
            if var in self._comps[i]:
                return ('comp', self._comps[i][var])
            if var in self._annots[i]:
                return ('annot', self._annots[i][var])
            if var in self._scopes[i]:
                return

    def _if_ret(self) -> Block:
        with self._local('__py2ai__funcret__'):
            return self.visit(ast.parse('if __py2ai__funcret__ == 2: break').body[0])

    def _nothing(self, node):
        return

    visit_ImportFrom = visit_Import = visit_Pass = _nothing

    def compile(self, root: ast.Module, collapsed: bool = True):
        self._ctx = {}
        self._procs = {}
        self._locals = set()
        self._global_assigns = {}
        self.project = BlocklyProject()
        self.visit(root)
        with open(LIB) as f:
            lib = BlocklyProject.from_xml(f.read())
        self.project.extend(lib)
        if collapsed:
            y = 0
            for blk in self.project:
                blk.y = y
                blk.collapsed = True
                y += 52
        return self.project

    def _add_component(
        self,
        type: str,
        name: str,
        parent: Optional[str] = None,
        version: Optional[Union[str, int]] = None,
        **kwargs: Any,
    ):
        if self._orig_schema is None:
            scn = app = 'Screen1'
        else:
            scn = self._orig_schema['Properties']['$Name']
            app = self._orig_schema['Properties']['AppName']
        if self._schema is None:
            self._schema = SCHEMA(scn, app)
        if parent:
            par = _find_comp(self._schema['Properties'], parent)
            if par is None:
                raise ValueError(f'Component {parent} not found')
        else:
            par = self._schema['Properties']
        comp = kwargs
        comp.update(
            {
                '$Name': name,
                '$Type': type,
                '$Version': version or VERSIONS[type],
                'Uuid': str(random.randint(-2147483648, 2147483647)),
            }
        )
        par.setdefault('$Components', []).append(comp)

    def _add_components(self, schema: dict):
        for comp in ADD_COMPONENTS:
            for exist in schema['Properties'].setdefault('$Components', []):
                if exist['$Name'] == comp['$Name']:
                    break
            else:
                schema['Properties']['$Components'].append(copy(comp))
        return schema

    def create(
        self,
        node: ast.Module,
        screen_name: str,
        app_name: Optional[str] = None,
        collapsed: bool = True,
    ):
        self._orig_schema = SCHEMA(screen_name, app_name)
        screen = Screen(
            BlocklyProject().to_xml().encode(),
            json.dumps(self._orig_schema).encode(),
            screen_name,
        )
        screen.blockly = self.compile(node, collapsed=collapsed)
        if self._schema is not None:
            screen.schema = self._schema
        self._add_components(screen.schema)
        return screen

    def update(self, screen: Screen, node: ast.Module, collapsed: bool = True):
        self._orig_schema = screen.schema
        screen.blockly = self.compile(node, collapsed=collapsed)
        if self._schema is not None:
            screen.schema = self._schema
        self._add_components(screen.schema)
        return screen

    def visit_Module(self, node):
        self._scopes.append(set())
        self._comps.append({})
        self._annots.append({})
        self._globals.append(set())
        for item in node.body:
            blk = self.visit(item)
            # print(blk)
            if blk is not None:
                self.project.append(blk)
        for var in self._scopes[-1]:
            blk = Block(
                'global_declaration',
                fields={'NAME': var},
                values={'VALUE': Block('text', fields={'TEXT': ''})},
            )
            self.project.append(blk)
        blk = self._set_var_block(
            '__py2ai__null__',
            Block(
                'component_method',
                mutations={
                    'component_type': 'Web',
                    'method_name': 'JsonTextDecodeWithDictionaries',
                    'is_generic': 'false',
                    'instance_name': '__py2ai__json__',
                },
                fields={'COMPONENT_SELECTOR': '__py2ai__json__'},
                values={'ARG0': Block('text', fields={'TEXT': 'null'})},
            ),
        )
        cur = blk
        for name, var_blk in self._global_assigns.items():
            cur.next = self._set_var_block(name, var_blk)
            while cur.next is not None:
                cur = cur.next
        for decl in self.project:
            if (
                decl.type == 'component_event'
                and decl.mutations
                and decl.mutations['component_type'] == 'Form'
                and decl.mutations['event_name'] == 'Initialize'
            ):
                cur.next = decl.statements['DO']
                decl.statements['DO'] = blk
                break
        else:
            for comp, cls in self._comps[-1].items():
                if cls is Form:
                    break
            else:
                raise NotSupportedError('No Screen (Form) component found')
            decl = Block(
                'component_event',
                mutations={
                    'component_type': 'Form',
                    'is_generic': 'false',
                    'instance_name': comp,
                    'event_name': 'Initialize',
                },
                fields={'COMPONENT_SELECTOR': comp},
                statements={'DO': blk},
            )
            self.project.append(decl)
        self._scopes.pop()
        self._comps.pop()
        self._annots.pop()
        self._globals.pop()
        return self.project

    def visit_Constant(self, node):
        if isinstance(node.value, bool):
            return Block(
                'logic_boolean',
                fields={'BOOL': ['FALSE', 'TRUE'][node.value]},
            )
        if isinstance(node.value, (int, float)):
            return Block('math_number', fields={'NUM': str(node.value)})
        if isinstance(node.value, str):
            return Block('text', fields={'TEXT': node.value})
        if node.value is None:
            return self._get_null_block()
        raise NotSupportedError(f'Constant with value {node.value!r}')

    def visit_List(self, node):
        return Block(
            'lists_create_with',
            mutations={'items': str(len(node.elts))},
            values={f'ADD{i}': self.visit(v) for i, v in enumerate(node.elts)},
        )

    def visit_Dict(self, node):
        assert len(node.keys) == len(node.values)
        elts = []
        for k, v in zip(node.keys, node.values):
            if k is None:
                raise NotSupportedError('Dict **values not supported')
            elts.append(
                Block('pair', values={'KEY': self.visit(k), 'VALUE': self.visit(v)})
            )
        return Block(
            'dictionaries_create_with',
            mutations={'items': str(len(elts))},
            values={f'ADD{i}': elts[i] for i in range(len(elts))},
        )

    def visit_Expr(self, node):
        val = self.visit(node.value)
        if val is None:
            return
        assert isinstance(val, Block)
        if val.type == 'component_method':
            mutations = val.mutations
            assert mutations is not None
            comp_type = mutations['component_type']
            comp_cls = getattr(components, comp_type)
            method_name = mutations['method_name']
            method = getattr(comp_cls, method_name)
            return_type = method.__annotations__['return']
            wrap = return_type is not None
        elif val.type == 'component_event':
            wrap = False
        else:
            wrap = True
        if wrap:
            return Block('controls_eval_but_ignore', values={'VALUE': val})
        return val

    def visit_Name(self, node):
        annot = self._get_annot(node.id)
        if annot and annot[0] == 'comp':
            return Block(
                'component_component_block',
                mutations={
                    'component_type': annot[1].__name__,
                    'instance_name': node.id,
                },
                fields={'COMPONENT_SELECTOR': node.id},
            )
        is_global = None
        if (
            not self._global
            and node.id not in self._scopes[-1]
            and node.id not in self._locals
        ):
            is_global = True
        return self._get_var_block(node.id, is_global)

    def visit_AnnAssign(self, node):
        if isinstance(node.annotation, ast.Name):
            ann = node.annotation.id
        elif isinstance(node.annotation, ast.Constant) and isinstance(
            node.annotation.value, str
        ):
            ann = node.annotation.value
        elif node.value is not None:
            return self.visit(ast.Assign(targets=[node.target], value=node.value))
        else:
            raise NotSupportedError('AnnAssign with unparsable annotation and no value')
        if not isinstance(node.target, ast.Name):
            raise NotSupportedError('AnnAssign target not a variable')
        var = node.target.id
        if (
            hasattr(components, ann)
            and issubclass(getattr(components, ann), Component)
            and (
                node.value is None
                or isinstance(node.value, ast.Name)
                and node.value.id == 'GetComponent'
            )
        ):
            # print('set comp', var)
            self._comps[-1][var] = getattr(components, ann)
        elif node.value is not None:
            self._annots[-1][var] = getattr(components, ann)
        if node.value is not None and not (
            isinstance(node.value, ast.Name) and node.value.id == 'GetComponent'
        ):
            return self.visit(ast.Assign(targets=[node.target], value=node.value))

    def visit_Assign(self, node):
        if len(node.targets) > 1:
            raise NotSupportedError('Assign has more than 1 targets')
        target = node.targets[0]
        if isinstance(target, ast.Subscript):
            return Block(
                'controls_eval_but_ignore',
                values={
                    'VALUE': self._get_proc_block(
                        '__py2ai__set_item__',
                        ['obj', 'key', 'value'],
                        [
                            self.visit(target.value),
                            self.visit(target.slice),
                            self.visit(node.value),
                        ],
                    )
                },
            )
        if isinstance(target, ast.Attribute):
            attr_obj = target.value
            if not isinstance(attr_obj, ast.Name):
                raise NotSupportedError('Assign attribute of non-variable')
            attr_var = attr_obj.id
            annot = self._get_annot(attr_var)
            if annot is None:
                raise NotSupportedError('Assign to an unannotated object attribute')
            annot_type, ann = annot
            if annot_type == 'comp' and hasattr(ann, target.attr):
                return Block(
                    'component_set_get',
                    mutations={
                        'component_type': ann.__name__,
                        'set_or_get': 'set',
                        'property_name': target.attr,
                        'is_generic': 'true',
                    },
                    fields={'PROP': target.attr},
                    values={
                        'COMPONENT': Block(
                            'component_component_block',
                            mutations={
                                'component_type': ann.__name__,
                                'instance_name': attr_var,
                            },
                            fields={'COMPONENT_SELECTOR': attr_var},
                        ),
                        'VALUE': self.visit(node.value),
                    },
                )
            if (
                annot_type == 'annot'
                and issubclass(ann, Component)
                and hasattr(ann, target.attr)
            ):
                return Block(
                    'component_set_get',
                    mutations={
                        'component_type': ann.__name__,
                        'set_or_get': 'set',
                        'property_name': target.attr,
                        'is_generic': 'true',
                    },
                    fields={'PROP': target.attr},
                    values={
                        'COMPONENT': self._get_var_block(attr_var),
                        'VALUE': self.visit(node.value),
                    },
                )
            raise NotSupportedError('Assign to a weirdly annotated object attribute')
        if isinstance(target, ast.Name):
            if target.id == '__py2ai__schema__':
                self._schema = ast.literal_eval(ast.unparse(node.value))
            elif (
                isinstance(node.value, ast.Call)
                and isinstance(node.value.func, ast.Name)
                and hasattr(components, node.value.func.id)
                and node.value.func.id != 'Component'
            ):
                call = node.value
                if call.args:
                    raise NotSupportedError('Assign Component must have no pos args')
                typ = node.value.func
                kws = {k.arg: k.value for k in call.keywords}
                if self._orig_schema is None:
                    scn = app = 'Screen1'
                else:
                    scn = self._orig_schema['Properties']['$Name']
                    app = self._orig_schema['Properties']['AppName']
                if self._schema is None:
                    self._schema = SCHEMA(scn, app)
                parent = self._schema['Properties']
                if typ.id == 'Form':
                    parent.update({k: str(ast.literal_eval(v)) for k, v in kws.items()})
                    self.visit(ast.AnnAssign(target=target, annotation=typ, value=None))
                    return
                if _find_comp(parent, target.id) is not None:
                    raise NotSupportedError('Assign Component duplicate component')
                if 'parent' in kws:
                    parent = kws.pop('parent')
                    if not isinstance(parent, ast.Name):
                        raise NotSupportedError(
                            'Assign Component parent must be variable'
                        )
                    parent = _find_comp(self._schema['Properties'], parent.id)
                    if parent is None:
                        raise NotSupportedError('Assign Component parent not found')
                kws = {k: str(ast.literal_eval(v)) for k, v in kws.items()}
                kws.update(
                    {
                        '$Name': target.id,
                        '$Type': typ.id,
                        '$Version': kws.pop('version', None) or VERSIONS[typ.id],
                        'Uuid': str(random.randint(-2147483648, 2147483647)),
                    }
                )
                parent.setdefault('$Components', []).append(kws)
                self.visit(ast.AnnAssign(target=target, annotation=typ, value=None))
                return
            elif (
                isinstance(node.value, ast.Call)
                and isinstance(node.value.func, ast.Name)
                and node.value.func.id == 'CreateComponent'
            ):
                call = node.value
                if len(call.args) != 1:
                    raise NotSupportedError(
                        'Assign CreateComponent must have 1 pos arg'
                    )
                typ = call.args[0]
                if not (
                    isinstance(typ, ast.Name)
                    and hasattr(components, typ.id)
                    and issubclass(getattr(components, typ.id), Component)
                    and typ.id != 'Component'
                ):
                    raise NotSupportedError('Assign CreateComponent invalid type')
                kws = {k.arg: k.value for k in call.keywords}
                if self._orig_schema is None:
                    scn = app = 'Screen1'
                else:
                    scn = self._orig_schema['Properties']['$Name']
                    app = self._orig_schema['Properties']['AppName']
                if self._schema is None:
                    self._schema = SCHEMA(scn, app)
                parent = self._schema['Properties']
                if typ.id == 'Form':
                    parent.update({k: str(ast.literal_eval(v)) for k, v in kws.items()})
                    self.visit(ast.AnnAssign(target=target, annotation=typ, value=None))
                    return
                if _find_comp(parent, target.id) is not None:
                    raise NotSupportedError(
                        'Assign CreateComponent duplicate component'
                    )
                if 'parent' in kws:
                    parent = kws.pop('parent')
                    if not isinstance(parent, ast.Name):
                        raise NotSupportedError(
                            'Assign CreateComponent parent must be variable'
                        )
                    parent = _find_comp(self._schema['Properties'], parent.id)
                    if parent is None:
                        raise NotSupportedError(
                            'Assign CreateComponent parent not found'
                        )
                kws = {k: str(ast.literal_eval(v)) for k, v in kws.items()}
                kws.update(
                    {
                        '$Name': target.id,
                        '$Type': typ.id,
                        '$Version': kws.pop('version', None) or VERSIONS[typ.id],
                        'Uuid': str(random.randint(-2147483648, 2147483647)),
                    }
                )
                parent.setdefault('$Components', []).append(kws)
                self.visit(ast.AnnAssign(target=target, annotation=typ, value=None))
                return
            else:
                if target.id not in self._globals[-1]:
                    self._scopes[-1].add(target.id)
                if self._global:
                    self._global_assigns[target.id] = self.visit(node.value)
                    return
                return self._set_var_block(
                    target.id,
                    self.visit(node.value),
                    True if target.id in self._globals[-1] else None,
                )
        raise NotSupportedError(f'Assign to {target.__class__.__name__} target')

    def visit_AugAssign(self, node):
        return self.visit(
            ast.Assign(
                targets=[node.target],
                value=ast.BinOp(left=node.target, op=node.op, right=node.value),
            )
        )

    def visit_Subscript(self, node):
        if isinstance(node.slice, ast.Slice):
            slice = node.slice
            return self._get_proc_block(
                '__py2ai__get_item_slice__',
                ['obj', 'start', 'end', 'step'],
                [
                    self.visit(node.value),
                    self.visit(slice.lower)
                    if slice.lower is not None
                    else self._get_null_block(),
                    self.visit(slice.upper)
                    if slice.upper is not None
                    else self._get_null_block(),
                    self.visit(slice.step)
                    if slice.step is not None
                    else self._get_null_block(),
                ],
            )
        return self._get_proc_block(
            '__py2ai__get_item__',
            ['obj', 'key'],
            [self.visit(node.value), self.visit(node.slice)],
        )

    def visit_Global(self, node):
        self._globals[-1].update(node.names)

    def visit_FunctionDef(self, node):
        args = [arg.arg for arg in node.args.posonlyargs + node.args.args]
        name = node.name
        self._procs[name] = args
        self._scopes.append({'__py2ai__return__'} | set(args))
        self._comps.append({})
        self._annots.append({})
        self._globals.append(set())
        blk = self.visit_nodes(node.body)
        local_vars = list(x for x in self._scopes[-1] if x not in args)
        # print('func', name, 'local vars', local_vars)
        for_ = Block(
            'controls_forRange',
            fields={'VAR': '__py2ai__funcret__'},
            values={
                'START': Block('math_number', fields={'NUM': '1'}),
                'END': Block('math_number', fields={'NUM': '1'}),
                'STEP': Block('math_number', fields={'NUM': '1'}),
            },
            statements={'DO': blk} if blk else None,
        )
        do = Block(
            'controls_do_then_return',
            values={'VALUE': self._get_var_block('__py2ai__return__')},
            statements={'STM': for_},
        )
        local_values = {
            f'DECL{i}': self._get_null_block() for i in range(len(local_vars))
        }
        local_values['RETURN'] = do
        local = Block(
            'local_declaration_expression',
            mutation_localnames=local_vars,
            fields={f'VAR{i}': a for i, a in enumerate(local_vars)},
            values=local_values,
        )
        proc_fields = {f'VAR{i}': a for i, a in enumerate(args)}
        proc_fields['NAME'] = name
        proc = Block(
            'procedures_defreturn',
            mutation_args=args,
            fields=proc_fields,
            values={'RETURN': local},
        )
        self._scopes.pop()
        self._comps.pop()
        self._annots.pop()
        self._globals.pop()
        return proc

    def visit_Return(self, node):
        blk = self._set_var_block(
            '__py2ai__funcret__', Block('math_number', fields={'NUM': '2'}), False
        )
        if node.value is not None:
            blk.chain(
                self._set_var_block('__py2ai__return__', self.visit(node.value), False)
            )
        return blk.chain(Block('controls_break'))

    def visit_Attribute(self, node):
        if not isinstance(node.value, ast.Name):
            raise NotSupportedError('Attribute of non-variable')
        if hasattr(enums, node.value.id):
            cls = getattr(enums, node.value.id)
            if issubclass(cls, enums.AI2Enum) and cls is not enums.AI2Enum:
                return Block(
                    'helpers_dropdown',
                    mutations={'key': node.value.id},
                    fields={'OPTION': getattr(cls, node.attr).value},
                )
            elif issubclass(cls, enums.AI2Helper) and cls is not enums.AI2Helper:
                return self.visit(ast.Constant(value=getattr(cls, node.attr)))
        var = node.value.id
        annot = self._get_annot(var)
        if annot is None:
            raise NotSupportedError('Attribute of unannotated variable')
        ann_type, ann = annot
        if ann_type == 'comp' and hasattr(ann, node.attr):
            return Block(
                'component_set_get',
                mutations={
                    'component_type': ann.__name__,
                    'set_or_get': 'get',
                    'property_name': node.attr,
                    'is_generic': 'true',
                },
                fields={'PROP': node.attr},
                values={
                    'COMPONENT': Block(
                        'component_component_block',
                        mutations={
                            'component_type': ann.__name__,
                            'instance_name': node.value.id,
                        },
                        fields={'COMPONENT_SELECTOR': node.value.id},
                    )
                },
            )
        if (
            ann_type == 'annot'
            and issubclass(ann, Component)
            and hasattr(ann, node.attr)
        ):
            return Block(
                'component_set_get',
                mutations={
                    'component_type': ann.__name__,
                    'set_or_get': 'get',
                    'property_name': node.attr,
                    'is_generic': 'true',
                },
                fields={'PROP': node.attr},
                values={'COMPONENT': self._get_var_block(node.value.id)},
            )

    def visit_Call(self, node):
        # node.args += [k.value for k in node.keywords]
        keywords = {k.arg: k.value for k in node.keywords if k.arg}
        if isinstance(node.func, ast.Attribute):
            attr_obj = node.func.value
            attr_attr = node.func.attr
            if attr_attr in METHODS:
                calls = METHODS[attr_attr]
                arg_len = len(node.args + node.keywords)
                if arg_len not in calls and -1 not in calls:
                    raise NotSupportedError('Call method with wrong argument count')
                call = calls[arg_len] if arg_len in calls else calls[-1]
                names, proc = call
                params = parse_args(names, node.args, keywords)
                args = [params[name] for name in names]
                return self._get_proc_block(
                    proc,
                    ['self'] + names,
                    [self.visit(attr_obj)] + [self.visit(param) for param in args],
                )
            if not isinstance(attr_obj, ast.Name):
                raise NotSupportedError('Call attribute of non-variable')
            attr_var = attr_obj.id
            if (attr_var, attr_attr) in ATTR_CALLS:
                calls = ATTR_CALLS[attr_var, attr_attr]
                arg_len = len(node.args + node.keywords)
                if arg_len not in calls and -1 not in calls:
                    raise NotSupportedError('Call function with wrong argument count')
                call = calls[arg_len] if arg_len in calls else calls[-1]
                names, func = call
                args = parse_args(names, node.args, keywords)
                return func(self, **args)
            is_event = attr_attr.startswith('on_')
            is_any_event = attr_attr.startswith('on_any_')
            if is_any_event:
                if (
                    not hasattr(components, attr_var)
                    or getattr(components, attr_var) is Component
                ):
                    raise NotSupportedError(
                        'Call any_event with non-Component subclass'
                    )
                spec = ast.parse(
                    getattr(
                        getattr(components, attr_var), attr_attr
                    ).__doc__.splitlines()[0],
                    mode='eval',
                )
                args = ['component', 'notAlreadyHandled'] + [
                    cast(ast.Name, x).id for x in cast(ast.Call, spec.body).args
                ]
                proc_obj = node.args[0]
                if not isinstance(proc_obj, ast.Name):
                    raise NotSupportedError('Call an event register with non-variable')
                proc_name = proc_obj.id
                if proc_name not in self._procs:
                    raise NotSupportedError('Call an event register with unbound var')
                proc_args = self._procs[proc_name]
                # print(args, proc_args)
                if len(args) != len(proc_args):
                    raise NotSupportedError('Call event register arg count mismatch')
                return Block(
                    'component_event',
                    mutations={
                        'component_type': attr_var,
                        'is_generic': 'true',
                        'event_name': attr_attr[7:],
                    },
                    statements={
                        'DO': Block(
                            'controls_eval_but_ignore',
                            values={
                                'VALUE': self._get_proc_block(
                                    proc_name,
                                    proc_args,
                                    [self._get_var_block(a, False, True) for a in args],
                                )
                            },
                        )
                    },
                )
            annot = self._get_annot(attr_var)
            if annot is None:
                raise NotSupportedError('Call an unannotated object attribute')
            annot_type, ann = annot
            if annot_type != 'comp':
                raise NotSupportedError('Call an event register without component')
            if not hasattr(ann, attr_attr):
                raise NotSupportedError('Call a nonexistent component method')
            if is_event:
                spec = ast.parse(
                    getattr(ann, attr_attr).__doc__.splitlines()[0], mode='eval'
                )
                args = [cast(ast.Name, x).id for x in cast(ast.Call, spec.body).args]
                proc_obj = node.args[0]
                if not isinstance(proc_obj, ast.Name):
                    raise NotSupportedError('Call an event register with non-variable')
                proc_name = proc_obj.id
                if proc_name not in self._procs:
                    raise NotSupportedError('Call an event register with unbound var')
                proc_args = self._procs[proc_name]
                # print(args, proc_args)
                if len(args) != len(proc_args):
                    raise NotSupportedError('Call event register arg count mismatch')
                return Block(
                    'component_event',
                    mutations={
                        'component_type': ann.__name__,
                        'is_generic': 'false',
                        'instance_name': attr_obj.id,
                        'event_name': attr_attr[3:],
                    },
                    fields={'COMPONENT_SELECTOR': attr_obj.id},
                    statements={
                        'DO': Block(
                            'controls_eval_but_ignore',
                            values={
                                'VALUE': self._get_proc_block(
                                    proc_name,
                                    proc_args,
                                    [self._get_var_block(a, False, True) for a in args],
                                )
                            },
                        )
                    },
                )
            return Block(
                'component_method',
                mutations={
                    'component_type': ann.__name__,
                    'method_name': attr_attr,
                    'is_generic': 'false',
                    'instance_name': attr_obj.id,
                },
                fields={'COMPONENT_SELECTOR': attr_obj.id},
                values={f'ARG{i}': self.visit(a) for i, a in enumerate(node.args)},
            )
        if not isinstance(node.func, ast.Name):
            raise NotSupportedError('Call a weird thing')
        if node.func.id in CALLS:
            calls = CALLS[node.func.id]
            arg_len = len(node.args + node.keywords)
            if arg_len not in calls and -1 not in calls:
                raise NotSupportedError('Call function with wrong argument count')
            call = calls[arg_len] if arg_len in calls else calls[-1]
            names, func = call
            args = parse_args(names, node.args, keywords)
            return func(self, **args)
        if node.func.id not in self._procs:
            raise NotSupportedError('Call a nonexistent procedure')
        return self._get_proc_block(
            node.func.id, self._procs[node.func.id], [self.visit(a) for a in node.args]
        )

    def visit_UnaryOp(self, node):
        if isinstance(node.op, ast.Not):
            return Block(
                'logic_negate',
                values={
                    'BOOL': self._get_proc_block(
                        '__py2ai__bool__', ['x'], [self.visit(node.operand)]
                    )
                },
            )
        if isinstance(node.op, ast.USub):
            return self.visit(
                ast.BinOp(left=ast.Constant(value=0), op=ast.Sub(), right=node.operand)
            )
        raise NotSupportedError(
            f'UnaryOp unsupported operator {node.op.__class__.__name__}'
        )

    def visit_BinOp(self, node):
        if isinstance(node.op, ast.Add):
            return self._get_proc_block(
                '__py2ai__add__',
                ['x', 'y'],
                [self.visit(node.left), self.visit(node.right)],
            )
        if isinstance(node.op, ast.Sub):
            return self._get_proc_block(
                '__py2ai__sub__',
                ['x', 'y'],
                [self.visit(node.left), self.visit(node.right)],
            )
        if isinstance(node.op, ast.Mult):
            return self._get_proc_block(
                '__py2ai__mul__',
                ['x', 'y'],
                [self.visit(node.left), self.visit(node.right)],
            )
        if isinstance(node.op, ast.Div):
            return self._get_proc_block(
                '__py2ai__truediv__',
                ['x', 'y'],
                [self.visit(node.left), self.visit(node.right)],
            )
        if isinstance(node.op, ast.FloorDiv):
            return self._get_proc_block(
                '__py2ai__floordiv__',
                ['x', 'y'],
                [self.visit(node.left), self.visit(node.right)],
            )
        if isinstance(node.op, ast.Mod):
            return self._get_proc_block(
                '__py2ai__mod__',
                ['x', 'y'],
                [self.visit(node.left), self.visit(node.right)],
            )
        raise NotSupportedError(
            f'BinOp unsupported operator {node.op.__class__.__name__}'
        )

    def visit_BoolOp(self, node):
        op = {ast.And: 'AND', ast.Or: 'OR', ast.AST: None}[node.op.__class__]
        return Block(
            'logic_operation',
            mutations={'items': str(len(node.values))},
            fields={'OP': op},
            values={
                (
                    'A' if i == 0 else 'B' if i == 1 else f'BOOL{i}'
                ): self._get_proc_block('__py2ai__bool__', ['x'], [self.visit(v)])
                for i, v in enumerate(node.values)
            },
        )

    def visit_Compare(self, node):
        if len(node.ops) > 1:
            return self.visit(
                ast.BoolOp(
                    op=ast.And(),
                    values=[
                        ast.Compare(left=l, ops=o, comparators=r)
                        for l, r, o in zip(
                            [node.left] + node.comparators, node.comparators, node.ops
                        )
                    ],
                )
            )
        left = node.left
        op = node.ops[0]
        right = node.comparators[0]
        if isinstance(op, ast.Eq):
            return self._get_proc_block(
                '__py2ai__eq__', ['x', 'y'], [self.visit(left), self.visit(right)]
            )
        if isinstance(op, ast.NotEq):
            return self._get_proc_block(
                '__py2ai__ne__', ['x', 'y'], [self.visit(left), self.visit(right)]
            )
        if isinstance(op, ast.Lt):
            return self._get_proc_block(
                '__py2ai__lt__', ['x', 'y'], [self.visit(left), self.visit(right)]
            )
        if isinstance(op, ast.Gt):
            return self._get_proc_block(
                '__py2ai__gt__', ['x', 'y'], [self.visit(left), self.visit(right)]
            )
        if isinstance(op, ast.LtE):
            return self._get_proc_block(
                '__py2ai__le__', ['x', 'y'], [self.visit(left), self.visit(right)]
            )
        if isinstance(op, ast.GtE):
            return self._get_proc_block(
                '__py2ai__ge__', ['x', 'y'], [self.visit(left), self.visit(right)]
            )
        if isinstance(op, ast.In):
            return self._get_proc_block(
                '__py2ai__contains__',
                ['obj', 'item'],
                [self.visit(right), self.visit(left)],  # wtf
            )
        raise NotSupportedError(f'Compare operator {op.__class__.__name__}')

    def visit_Raise(self, node):
        if isinstance(node.exc, ast.Name):
            if node.exc.id == 'CloseScreen':
                return Block('controls_closeScreen')
            if node.exc.id == 'CloseApplication':
                return Block('controls_closeApplication')
        raise NotSupportedError('Raise exception not supported')

    def visit_If(self, node):
        ifs = [node]
        while len(ifs[-1].orelse) == 1 and isinstance(ifs[-1].orelse[0], ast.If):
            ifs.append(ifs[-1].orelse[0])
        elifs = len(ifs) - 1
        dos = {}
        for i, if_ in enumerate(ifs):
            blk = self.visit_nodes(if_.body)
            if blk:
                dos[f'DO{i}'] = blk
        if ifs[-1].orelse:
            blk = self.visit_nodes(ifs[-1].orelse)
            if blk:
                dos['ELSE'] = blk
        return Block(
            'controls_if',
            mutations={'elseif': str(elifs), 'else': '1' if ifs[-1].orelse else '0'},
            values={
                f'IF{i}': self._get_proc_block(
                    '__py2ai__bool__', ['x'], [self.visit(x.test)]
                )
                for i, x in enumerate(ifs)
            },
            statements=dos,
        )

    def visit_Break(self, node):
        cast(None, node)
        return Block('controls_break')

    def visit_For(self, node):
        if node.orelse:
            raise NotSupportedError('For else statement')
        if not isinstance(node.target, ast.Name):
            raise NotSupportedError('For target not a variable')
        if (
            isinstance(node.iter, ast.Call)
            and isinstance(node.iter.func, ast.Name)
            and node.iter.func.id == 'range'
            and 1 <= len(node.iter.args) <= 3
        ):
            args = node.iter.args
            step = args[2] if len(args) == 3 else ast.Constant(value=1)
            blk = self.visit_nodes(node.body)
            return Block(
                'controls_forRange',
                fields={'VAR': node.target.id},
                values={
                    'START': self.visit(args[0])
                    if len(args) > 1
                    else Block('math_number', fields={'NUM': '0'}),
                    'END': Block(
                        'math_add',
                        mutations={'items': '2'},
                        values={
                            'NUM0': self.visit(args[0])
                            if len(args) == 1
                            else self.visit(args[1]),
                            'NUM1': Block(
                                'controls_choose',
                                values={
                                    'TEST': self.visit(
                                        ast.Compare(
                                            left=step,
                                            ops=[ast.Lt()],
                                            comparators=[ast.Constant(value=0)],
                                        )
                                    ),
                                    'THENRETURN': Block(
                                        'math_number', fields={'NUM': '1'}
                                    ),
                                    'ELSERETURN': Block(
                                        'math_number', fields={'NUM': '-1'}
                                    ),
                                },
                            ),
                        },
                    ),
                    'STEP': self.visit(step),
                },
                statements={'DO': blk} if blk else None,
            ).chain(self._if_ret())
        with self._local(node.target.id):
            blk = self.visit_nodes(node.body)
            return Block(
                'controls_forEach',
                fields={'VAR': node.target.id},
                values={
                    'LIST': self._get_proc_block(
                        '__py2ai__iter__', ['x'], [self.visit(node.iter)]
                    )
                },
                statements=blk and {'DO': blk},
            ).chain(self._if_ret())
