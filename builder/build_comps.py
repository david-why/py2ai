from typing import TYPE_CHECKING
import ast, json


def ast_dumps(data):
    if isinstance(data, dict):
        keys = []
        values = []
        for k, v in data.items():
            keys.append(ast_dumps(k))
            values.append(ast_dumps(v))
        return ast.Dict(keys=keys, values=values)
    elif isinstance(data, list):
        return ast.List(elts=[ast_dumps(x) for x in data], ctx=ast.Load())
    elif isinstance(data, (str, int, float, bool, type(None))):
        return ast.Constant(value=data)
    else:
        raise TypeError(data)


def _function(*args, **kwargs):
    return ast.FunctionDef(*args, **kwargs, lineno=0)


with open('components.json') as f:
    pages = json.load(f)

TYPES = {'str': str, 'int': int, 'bool': bool, 'list': list, 'dict': dict}
not_implemented = ast.parse('raise NotImplementedError').body[0]
Component_def = '''\
class Component:
    __data__: ClassVar[dict]
    def __init__(self, *, children=None, **kwargs):
        self._children = children
        for prop in self.__data__['properties']:
            if not prop['bo']:
                setattr(self, prop['name'], kwargs.pop(prop['name']))
        if kwargs:
            raise ValueError(kwargs)'''
Component = ast.parse(Component_def).body[0]

stmts = [
    ast.ImportFrom(module=None, names=[ast.alias(name='enums')], level=1),
    ast.ImportFrom(
        module='typing',
        names=[ast.alias(name=name) for name in ['Any', 'Callable', 'ClassVar']],
        level=0,
    ),
    Component,
]
for page in pages:
    print(f'building page {page["name"]}')
    for comp_name, comp in page['contents'].items():
        comp_name = comp_name if comp_name != 'Screen' else 'Form'
        print(f'building component {comp_name}')
        cls = ast.ClassDef(
            name=comp_name,
            bases=[ast.Name(id='Component', ctx=ast.Load())],
            keywords=[],
            body=[
                ast.Expr(value=ast.Constant(value=comp['desc'])),
                ast.Assign(
                    targets=[ast.Name(id='__data__', ctx=ast.Store())],
                    value=ast_dumps(comp),
                    lineno=0,
                )
            ],
            decorator_list=[],
        )
        init = _function(
            name='__init__',
            args=ast.arguments(
                args=[],
                posonlyargs=[ast.arg(arg='self')],
                kwonlyargs=[
                    ast.arg(
                        arg='parent',
                        annotation=ast.Name(id='Component', ctx=ast.Load()),
                    )
                ],
                defaults=[],
                kw_defaults=[ast.Constant(value=...)],
            ),
            body=[not_implemented],
            decorator_list=[],
        )
        cls.body.append(init)
        for prop in comp['properties']:
            prop_name = prop['name']
            if prop['do'] or not prop['bo']:
                init.args.kwonlyargs.append(
                    ast.arg(
                        arg=prop_name,
                        annotation=ast.Name(id=prop['type'], ctx=ast.Load()),
                    )
                )
                init.args.kw_defaults.append(ast.Constant(value=...))
            if prop['do']:
                continue
            print(f'building property {prop_name}')
            stmt = _function(
                name=prop_name,
                args=ast.arguments(
                    args=[ast.arg(arg='self')],
                    posonlyargs=[],
                    kwonlyargs=[],
                    defaults=[],
                ),
                body=[
                    ast.Expr(value=ast.Constant(value=prop['desc'])),
                    not_implemented,
                ],
                decorator_list=[ast.Name(id='property', ctx=ast.Load())],
                returns=ast.Name(id=prop['type'], ctx=ast.Load()),
            )
            cls.body.append(stmt)
            if not prop['ro']:
                stmt = _function(
                    name=prop_name,
                    args=ast.arguments(
                        args=[],
                        posonlyargs=[
                            ast.arg(arg='self', annotation=None),
                            ast.arg(
                                arg='value',
                                annotation=ast.Name(id=prop['type'], ctx=ast.Load()),
                            ),
                        ],
                        kwonlyargs=[],
                        defaults=[],
                    ),
                    body=[not_implemented],
                    decorator_list=[
                        ast.Attribute(
                            value=ast.Name(id=prop_name, ctx=ast.Load()),
                            attr='setter',
                            ctx=ast.Load(),
                        )
                    ],
                    returns=ast.Name(id='None', ctx=ast.Load()),
                )
                cls.body.append(stmt)
        for method in comp['methods']:
            method_name = method['name']
            print(f'building method {method_name}')
            stmt = _function(
                name=method_name,
                args=ast.arguments(
                    args=[],
                    posonlyargs=[ast.arg(arg='self', annotation=None)]
                    + [
                        ast.arg(
                            arg=x['name'] + ('_' if x['name'] in ['from'] else ''),
                            annotation=ast.Name(id=x['type'], ctx=ast.Load()),
                        )
                        for x in method['args']
                    ],
                    kwonlyargs=[],
                    defaults=[],
                ),
                body=[ast.Expr(value=ast.Constant(value=method['desc'])), not_implemented],
                decorator_list=[],
                returns=ast.Name(id=method['returns'] or 'None', ctx=ast.Load()),
            )
            cls.body.append(stmt)
        for event in comp['events']:
            event_name = event['name']
            print(f'building event {event_name}')
            doc = f'{event_name}({", ".join(x["name"] for x in event["args"])})\n\n'
            doc += event['desc']
            stmt = _function(
                name=f'on_{event_name}',
                args=ast.arguments(
                    args=[],
                    posonlyargs=[
                        ast.arg(arg='self', annotation=None),
                        ast.arg(
                            arg='callback',
                            annotation=ast.Subscript(
                                value=ast.Name(id='Callable', ctx=ast.Load()),
                                slice=ast.Tuple(
                                    elts=[
                                        ast.List(
                                            elts=[
                                                ast.Name(id=x['type'], ctx=ast.Load())
                                                for x in event['args']
                                            ],
                                            ctx=ast.Load(),
                                        ),
                                        ast.Name(id='None', ctx=ast.Load()),
                                    ],
                                    ctx=ast.Load(),
                                ),
                                ctx=ast.Load(),
                            ),
                        ),
                    ],
                    kwonlyargs=[],
                    defaults=[],
                ),
                body=[ast.Expr(value=ast.Constant(value=doc)), not_implemented],
                decorator_list=[],
                returns=ast.Name(id='None', ctx=ast.Load()),
            )
            cls.body.append(stmt)
            stmt = _function(
                name=f'on_any_{event_name}',
                args=ast.arguments(
                    args=[],
                    posonlyargs=[
                        ast.arg(
                            arg='callback',
                            annotation=ast.Subscript(
                                value=ast.Name(id='Callable', ctx=ast.Load()),
                                slice=ast.Tuple(
                                    elts=[
                                        ast.List(
                                            elts=[
                                                ast.Constant(value=comp_name),
                                                ast.Name(id='bool', ctx=ast.Load()),
                                            ]
                                            + [
                                                ast.Name(id=x['type'], ctx=ast.Load())
                                                for x in event['args']
                                            ],
                                            ctx=ast.Load(),
                                        ),
                                        ast.Name(id='None', ctx=ast.Load()),
                                    ],
                                    ctx=ast.Load(),
                                ),
                                ctx=ast.Load(),
                            ),
                        ),
                    ],
                    kwonlyargs=[],
                    defaults=[],
                ),
                body=[ast.Expr(value=ast.Constant(value=doc)), not_implemented],
                decorator_list=[ast.Name(id='staticmethod', ctx=ast.Load())],
                returns=ast.Name(id='None', ctx=ast.Load()),
            )
            cls.body.append(stmt)
        stmts.append(cls)

with open('components.py', 'w') as f:
    # vis = ast._Unparser()
    # vis._source = []
    # vis.traverse(ast.Module(body=stmts, type_ignores=[]))
    # print(vis._source)
    f.write(ast.unparse(ast.Module(body=stmts, type_ignores=[])))
