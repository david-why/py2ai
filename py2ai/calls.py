import ast
import builtins
import os
import random as _random
import string
from typing import Callable, Dict, List, Literal, Optional, Tuple, Union

from .blockly import Block

Func = Callable[..., Block]
Call = Tuple[List[str], Func]

CALLS: Dict[str, Dict[int, Call]] = {}
ATTR_CALLS: Dict[Tuple[str, str], Dict[int, Call]] = {}
METHODS: Dict[str, Dict[int, Tuple[List[str], str]]] = {}


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


def _mregister(method: str, args: List[str], name: Optional[str] = None):
    METHODS.setdefault(method, {})[len(args)] = (
        args,
        name or f'__py2ai__meth__{method}__',
    )


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


@_register(['__value'])
def bool(comp, __value):
    return comp._get_proc_block('__py2ai__bool__', ['x'], [comp.visit(__value)])


@_register(['__value'], 'len')
def _len(comp, __value):
    return comp._get_proc_block('__py2ai__len__', ['obj'], [comp.visit(__value)])


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
def min(comp, *args):
    return Block(
        'lists_minimum_value',
        fields={'VAR1': 'item1', 'VAR2': 'item2'},
        values={
            'LIST': comp.visit(ast.List(elts=list(args), ctx=ast.Load())),
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
def max1(comp, __iterable):
    return Block(
        'lists_maximum_value',
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
def max(comp, *args):
    return Block(
        'lists_maximum_value',
        fields={'VAR1': 'item1', 'VAR2': 'item2'},
        values={
            'LIST': comp.visit(ast.List(elts=list(args), ctx=ast.Load())),
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


@_register(['url'])
@_register(['url', 'callback'])
@_register(['url', 'callback', 'headers'])
def web_get(comp, **kwargs):
    return _web_request(comp, 'Get', **kwargs)


@_register(['url'])
@_register(['url', 'callback'])
@_register(['url', 'callback', 'data'])
@_register(['url', 'callback', 'data', 'headers'])
def web_post(comp, **kwargs):
    return _web_request(comp, 'PostText', **kwargs)


@_register(['url'])
@_register(['url', 'callback'])
@_register(['url', 'callback', 'headers'])
def web_delete(comp, **kwargs):
    return _web_request(comp, 'Delete', **kwargs)


@_register(['text'])
def obfs_text(comp, text):
    blk = comp._visit(text)
    if blk.type != 'text':
        raise ValueError('obfs_text argument must be a literal string')
    return Block(
        'obfuscated_text',
        mutations={'confounder': ''.join(_random.choices(string.ascii_lowercase, k=8))},
        fields={'TEXT': blk.fields['TEXT']},
    )


@_register(['name'])
def get_compile_env(comp, name):
    if not isinstance(name, ast.Constant) or not isinstance(name.value, builtins.str):
        raise ValueError('get_compile_env argument must be a literal string')
    return comp._visit(ast.Constant(value=os.environ[name.value]))


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


@_aregister('random', ['a', 'b'])
def randint(comp, a, b):
    return Block('math_random_int', values={'FROM': comp.visit(a), 'TO': comp.visit(b)})


@_aregister('random', ['seq'])
def choice(comp, seq):
    return Block(
        'lists_pick_random_item',
        values={
            'LIST': comp._get_proc_block('__py2ai__iter__', ['x'], [comp.visit(seq)])
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


@_aregister('time')
def time(comp):
    return Block(
        'math_division',
        values={
            'A': Block(
                'component_method',
                mutations={
                    'component_type': 'Clock',
                    'method_name': 'SystemTime',
                    'is_generic': 'false',
                    'instance_name': '__py2ai__clock__',
                },
                fields={'COMPONENT_SELECTOR': '__py2ai__clock__'},
            ),
            'B': Block('math_number', fields={'NUM': '1000'}),
        },
    )


@_aregister('time', ['seconds'], 'localtime')
def localtime1(comp, seconds):
    return comp._get_proc_block(
        '__py2ai__localtime__', ['seconds'], [comp._visit(seconds)]
    )


@_aregister('time', [], 'localtime')
def localtime0(comp):
    return comp._get_proc_block('__py2ai__localtime__', ['seconds'], [time(comp)])


@_aregister('time', ['format', 'tuple'], 'strftime')
def strftime2(comp, format, tuple):
    return comp._get_proc_block(
        '__py2ai__strftime__',
        ['format', 'tuple'],
        [comp._visit(format), comp._visit(tuple)],
    )


@_aregister('time', ['format'], 'strftime')
def strftime1(comp, format):
    return comp._get_proc_block(
        '__py2ai__strftime__',
        ['format', 'tuple'],
        [comp._visit(format), localtime0(comp)],
    )


_mregister('append', ['x'])
_mregister('clear', [])
_mregister('copy', [])
_mregister('count', ['x'])
_mregister('extend', ['x'])
_mregister('index', ['x', 'start', 'stop'], '__py2ai__meth__index__3__')
_mregister('index', ['x', 'start'], '__py2ai__meth__index__2__')
_mregister('index', ['x'], '__py2ai__meth__index__1__')
_mregister('insert', ['i', 'x'])
_mregister('pop', ['x'])
_mregister('remove', ['x'])
_mregister('reverse', [])
