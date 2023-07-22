import ast
from typing import TYPE_CHECKING, Callable, Dict, List, Literal, Optional, Tuple, Union
import random as _random, string
import builtins
from .blockly import Block

if TYPE_CHECKING:
    from .compiler import PythonCompiler

# Call = Callable[['PythonCompiler', List[ast.expr]], Block]
Func = Callable[..., Block]
Call = Tuple[List[str], Func]

CALLS: Dict[str, Dict[int, Call]] = {}
ATTR_CALLS: Dict[Tuple[str, str], Dict[int, Call]] = {}


def _register(
    args: Union[List[str], Literal[-1]] = [], name: Optional[str] = None
) -> Callable[[Func], Func]:
    def deco(func: Func):
        CALLS.setdefault(name or func.__name__, {})[-1 if args == -1 else len(args)] = (
            args if args != -1 else [],
            func,
        )
        return func

    return deco


def _aregister(
    module: str, args: Union[List[str], Literal[-1]] = [], name: Optional[str] = None
) -> Callable[[Func], Func]:
    def deco(func: Func):
        ATTR_CALLS.setdefault((module, name or func.__name__), {})[
            -1 if args == -1 else len(args)
        ] = (args if args != -1 else [], func)
        return func

    return deco


@_register(['__value'])
def int(comp, __value):
    return Block(
        'math_add',
        mutations={'items': '2'},
        values={
            'NUM0': comp.visit(__value),
            'NUM1': Block('math_number', fields={'NUM': '0'}),
        },
    )


@_register(['__value'])
def str(comp, __value):
    return comp._get_proc_block('__py2ai__str__', ['x'], [comp.visit(__value)])


@_register(['stop'], 'range')
def range1(comp, stop):
    return comp._get_proc_block(
        '__py2ai__range__',
        ['start', 'stop', 'step'],
        [
            Block('math_number', fields={'NUM': '0'}),
            comp.visit(stop),
            Block('math_number', fields={'NUM': '1'}),
        ],
    )


@_register(['start', 'stop'], 'range')
def range2(comp, start, stop):
    return comp._get_proc_block(
        '__py2ai__range__',
        ['start', 'stop', 'step'],
        [
            comp.visit(start),
            comp.visit(stop),
            Block('math_number', fields={'NUM': '1'}),
        ],
    )


@_register(['start', 'stop', 'step'], 'range')
def range3(comp, args):
    return comp._get_proc_block(
        '__py2ai__range__',
        ['start', 'stop', 'step'],
        [comp.visit(args[0]), comp.visit(args[1]), comp.visit(args[2])],
    )


@_register(['__iterable'], 'min')
def min1(comp, __iterable):
    return Block(
        'lists_minimum_value',
        fields={'VAR1': 'item1', 'VAR2': 'item2'},
        values={
            'LIST': comp._get_proc_block(
                '__py2ai__iter__', ['x'], [comp.visit(__iterable)]
            ),
            'COMPARE': comp._get_proc_block(
                '__py2ai__lt__',
                ['x', 'y'],
                [
                    comp._get_var_block('item1', False),
                    comp._get_var_block('item2', False),
                ],
            ),
        },
    )


@_register(-1)
def min(comp, args):
    return Block(
        'lists_minimum_value',
        fields={'VAR1': 'item1', 'VAR2': 'item2'},
        values={
            'LIST': comp.visit(ast.List(elts=args, ctx=ast.Load())),
            'COMPARE': comp._get_proc_block(
                '__py2ai__lt__',
                ['x', 'y'],
                [
                    comp._get_var_block('item1', False),
                    comp._get_var_block('item2', False),
                ],
            ),
        },
    )


@_register(['__iterable'], 'max')
def max1(comp, args):
    return Block(
        'lists_maximum_value',
        fields={'VAR1': 'item1', 'VAR2': 'item2'},
        values={
            'LIST': comp._get_proc_block(
                '__py2ai__iter__', ['x'], [comp.visit(args[0])]
            ),
            'COMPARE': comp._get_proc_block(
                '__py2ai__lt__',
                ['x', 'y'],
                [
                    comp._get_var_block('item1', False),
                    comp._get_var_block('item2', False),
                ],
            ),
        },
    )


@_register(-1)
def max(comp, args):
    return Block(
        'lists_maximum_value',
        fields={'VAR1': 'item1', 'VAR2': 'item2'},
        values={
            'LIST': comp.visit(ast.List(elts=args, ctx=ast.Load())),
            'COMPARE': comp._get_proc_block(
                '__py2ai__lt__',
                ['x', 'y'],
                [
                    comp._get_var_block('item1', False),
                    comp._get_var_block('item2', False),
                ],
            ),
        },
    )


def _web_request(comp, method, url, callback=None, data=None, headers=None):
    num = comp._ctx.setdefault('calls.webrequest.num', 1)
    name = f'__py2ai__Web{num}__'
    comp._ctx['calls.webrequest.num'] += 1
    comp._add_component('Web', name)
    if callback is not None:
        if not isinstance(callback, ast.Name):
            raise TypeError('Callback not a procedure name')
        if callback.id not in comp._procs:
            raise ValueError(f'Callback procedure {callback.id} not found')
        comp.project.append(
            Block(
                'component_event',
                mutations={
                    'component_type': 'Web',
                    'is_generic': 'false',
                    'instance_name': name,
                    'event_name': 'GotText',
                },
                fields={'COMPONENT_SELECTOR': name},
                statements={
                    'DO': Block(
                        'controls_eval_but_ignore',
                        values={
                            'VALUE': comp._get_proc_block(
                                callback.id,
                                comp._procs[callback.id],
                                [
                                    Block(
                                        'lexical_variable_get',
                                        fields={'VAR': 'responseCode'},
                                    ),
                                    Block(
                                        'lexical_variable_get',
                                        fields={'VAR': 'responseContent'},
                                    ),
                                ],
                            )
                        },
                    )
                },
            )
        )
    blk = Block(
        'component_set_get',
        mutations={
            'component_type': 'Web',
            'set_or_get': 'set',
            'property_name': 'Url',
            'is_generic': 'true',
        },
        fields={'PROP': 'Url'},
        values={
            'COMPONENT': Block(
                'component_component_block',
                mutations={'component_type': 'Web', 'instance_name': name},
                fields={'COMPONENT_SELECTOR': name},
            ),
            'VALUE': comp.visit(url),
        },
    )
    cur = blk
    if headers is not None:
        cur.next = Block(
            'component_set_get',
            mutations={
                'component_type': 'Web',
                'set_or_get': 'set',
                'property_name': 'RequestHeaders',
                'is_generic': 'true',
            },
            fields={'PROP': 'RequestHeaders'},
            values={
                'COMPONENT': Block(
                    'component_component_block',
                    mutations={'component_type': 'Web', 'instance_name': name},
                    fields={'COMPONENT_SELECTOR': name},
                ),
                'VALUE': comp.visit(headers),
            },
        )
        cur = cur.next
    values = {'ARG0': Block('text', fields={'TEXT': ''})}
    if data is not None:
        values['ARG0'] = comp.visit(data)
    cur.next = Block(
        'component_method',
        mutations={
            'component_type': 'Web',
            'method_name': method,
            'is_generic': 'false',
            'instance_name': name,
        },
        fields={'COMPONENT_SELECTOR': name},
        values=values,
    )
    return Block(
        'controls_do_then_return',
        statements={'STM': blk},
        values={'VALUE': comp._get_null_block()},
    )
    return Block(
        'component_method',
        mutations={
            'component_type': 'Web',
            'method_name': 'JsonTextDecodeWithDictionaries',
            'is_generic': 'false',
            'instance_name': '__py2ai__json__',
        },
        fields={'COMPONENT_SELECTOR': '__py2ai__json__'},
        values={'ARG0': Block('text', fields={'TEXT': 'null'})},
    )


@_register(['url'])
@_register(['url', 'callback'])
@_register(['url', 'callback', 'headers'])
def web_get(comp, **kwargs):
    return _web_request(comp, 'Get', **kwargs)


@_register(['url'])
@_register(['url', 'callback'])
@_register(['url', 'callback', 'headers'])
def web_delete(comp, **kwargs):
    return _web_request(comp, 'Delete', **kwargs)


@_register(['text'])
def obfs_text(comp, text):
    if not isinstance(text, ast.Constant) or not isinstance(text.value, builtins.str):
        raise ValueError('obfs_text argument must be a literal string')
    return Block(
        'obfuscated_text',
        mutations={'confounder': ''.join(_random.choices(string.ascii_lowercase, k=8))},
        fields={'TEXT': text.value}
    )


@_aregister('random')
def random(comp):
    return Block('math_random_float')


@_aregister('random', ['stop'], 'randrange')
def randrange1(comp, stop):
    return Block(
        'math_random_int',
        values={
            'FROM': Block('math_number', fields={'NUM': '0'}),
            'TO': comp.visit(
                ast.BinOp(left=stop, op=ast.Sub(), right=ast.Constant(value=1))
            ),
        },
    )


@_aregister('random', ['start', 'stop'], 'randrange')
def randrange2(comp, start, stop):
    return Block(
        'math_random_int',
        values={
            'FROM': comp.visit(start),
            'TO': comp.visit(
                ast.BinOp(left=stop, op=ast.Sub(), right=ast.Constant(value=1))
            ),
        },
    )


@_aregister('json', ['obj'])
def dumps(comp, obj):
    return Block(
        'component_method',
        mutations={
            'component_type': 'Web',
            'method_name': 'JsonObjectEncode',
            'is_generic': 'false',
            'instance_name': '__py2ai__json__',
        },
        fields={'COMPONENT_SELECTOR': '__py2ai__json__'},
        values={'ARG0': comp.visit(obj)},
    )


@_aregister('json', ['s'])
def loads(comp, s):
    return Block(
        'component_method',
        mutations={
            'component_type': 'Web',
            'method_name': 'JsonTextDecodeWithDictionaries',
            'is_generic': 'false',
            'instance_name': '__py2ai__json__',
        },
        fields={'COMPONENT_SELECTOR': '__py2ai__json__'},
        values={'ARG0': comp.visit(s)},
    )
