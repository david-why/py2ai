from collections.abc import MutableSequence
from typing import Dict, List, Optional

from lxml import etree as ET
from lxml.etree import Element as E
from lxml.etree import SubElement as S

type_ = type


class BlocklyProject(MutableSequence['Block']):
    def __init__(self, blocks: Optional[List['Block']] = None) -> None:
        self.blocks = blocks or []

    def __getitem__(self, index: int) -> 'Block':
        return self.blocks[index]

    def __setitem__(self, index: int, value: 'Block') -> None:
        self.blocks[index] = value

    def __delitem__(self, index: int) -> None:
        del self.blocks[index]

    def __len__(self) -> int:
        return len(self.blocks)

    def insert(self, index: int, value: 'Block') -> None:
        self.blocks.insert(index, value)

    def _to_xml(self):
        root = E('xml', xmlns='http://www.w3.org/1999/xhtml')
        for block in self.blocks:
            root.append(block._to_xml())
        S(root, 'yacodeblocks', {'ya-version': '223', 'language-version': '36'})
        return root

    def to_xml(self) -> str:
        return ET.tostring(self._to_xml()).replace(b'\n', b'&#10;').decode()

    @classmethod
    def _from_xml(cls, xml):
        blocks = []
        for child in xml.iterchildren('{*}block'):
            blk = Block._from_xml(child)
            blocks.append(blk)
        return cls(blocks)

    @classmethod
    def from_xml(cls, xml: str) -> 'BlocklyProject':
        if not xml:
            return cls()
        root = ET.fromstring(xml)
        return cls._from_xml(root)


class Block:
    NEXT_ID = 1

    def __init__(
        self,
        type: str,
        x: int = 0,
        y: int = 0,
        id: Optional[str] = None,
        mutations: Optional[Dict[str, str]] = None,
        mutation_args: Optional[List[str]] = None,
        mutation_localnames: Optional[List[str]] = None,
        mutation_eventparams: Optional[List[str]] = None,
        fields: Optional[Dict[str, str]] = None,
        values: Optional[Dict[str, 'Block']] = None,
        statements: Optional[Dict[str, 'Block']] = None,
        next: Optional['Block'] = None,
    ) -> None:
        self.type = type
        self.x = x
        self.y = y
        self.mutations = mutations
        self.mutation_args = mutation_args
        self.mutation_localnames = mutation_localnames
        self.mutation_eventparams = mutation_eventparams
        self.fields = fields or {}
        self.values = values or {}
        self.statements = statements or {}
        self.next = next
        self.id = id
        if id is None:
            self.id = str(type_(self).NEXT_ID)
            type_(self).NEXT_ID += 1

    def _to_xml(self):
        block = E('block', type=self.type, id=self.id, x=str(self.x), y=str(self.y))
        if (
            self.mutations is not None
            or self.mutation_args is not None
            or self.mutation_localnames is not None
            or self.mutation_eventparams is not None
        ):
            mutation = S(
                block,
                'mutation',
                {k: str(v) for k, v in (self.mutations or {}).items()},
            )
            if self.mutation_args is not None:
                for name in self.mutation_args:
                    S(mutation, 'arg', name=name)
            if self.mutation_localnames is not None:
                for name in self.mutation_localnames:
                    S(mutation, 'localname', name=name)
            if self.mutation_eventparams is not None:
                for name in self.mutation_eventparams:
                    S(mutation, 'eventparam', name=name)
        for name, value in self.fields.items():
            field = S(block, 'field', name=name)
            field.text = value
        for name, value in self.values.items():
            val = S(block, 'value', name=name)
            val.append(value._to_xml())
        for name, value in self.statements.items():
            statement = S(block, 'statement', name=name)
            statement.append(value._to_xml())
        if self.next is not None:
            next = S(block, 'next')
            next.append(self.next._to_xml())
        return block

    def to_xml(self) -> str:
        return ET.tostring(self._to_xml()).replace(b'\n', b'&#10;').decode()

    @classmethod
    def _from_xml(cls, xml):
        kwargs = {
            'type': xml.get('type'),
            'x': int(xml.get('x', 0)),
            'y': int(xml.get('y', 0)),
            'id': xml.get('id'),
        }
        for child in xml:
            if child.tag.endswith('mutation'):
                kwargs['mutations'] = dict(child.items())
                for c in child:
                    if c.tag.endswith('arg'):
                        kwargs.setdefault('mutation_args', []).append(c.get('name'))
                    elif c.tag.endswith('localname'):
                        kwargs.setdefault('mutation_localnames', []).append(
                            c.get('name')
                        )
            elif child.tag.endswith('field'):
                kwargs.setdefault('fields', {})[child.get('name')] = child.text
            elif child.tag.endswith('value'):
                kwargs.setdefault('values', {})[child.get('name')] = Block._from_xml(
                    child[0]
                )
            elif child.tag.endswith('statement'):
                kwargs.setdefault('statements', {})[
                    child.get('name')
                ] = Block._from_xml(child[0])
            elif child.tag.endswith('next'):
                kwargs['next'] = Block._from_xml(child[0])
        return cls(**kwargs)

    @classmethod
    def from_xml(cls, xml: str) -> 'Block':
        return cls._from_xml(ET.fromstring(xml))
