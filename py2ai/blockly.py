from collections.abc import MutableSequence
from typing import Dict, List, Optional

from lxml import etree as ET
from lxml.etree import Element as E
from lxml.etree import SubElement as S

type_ = type


class BlocklyProject(MutableSequence['Block']):
    """Represents a Blockly project, or a list of Blocks."""

    def __init__(self, blocks: Optional[List['Block']] = None) -> None:
        """
        Create a BlocklyProject.
        :param blocks: The initial list of blocks.
        """
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
        """
        Returns the XML representation of the project. This is the format of the .bky
        files.
        :return: The XML representation.
        """
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
        """
        Create a BlocklyProject from the XML format, or the .bky file.
        :param xml: The XML string.
        :return: A created BlocklyProject.
        """
        if not xml:
            return cls()
        root = ET.fromstring(xml)
        return cls._from_xml(root)


class Block:
    """Represents a Blockly block."""

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
        collapsed: bool = False,
        next: Optional['Block'] = None,
    ) -> None:
        """
        Create a Block.
        :param type: The type of the block.
        :param x: The x-coordinates of the block.
        :param y: The y-coordinates of the block.
        :param id: The ID of the block. This will be generated if not given.
        :param mutations: The mutations on the block. These are the attributes on the
        "mutation" XML tag.
        :param mutation_args: The "name" attribute of "arg" tags within the "mutation"
        tag.
        :param mutation_localnames: The "name" attribute of "localname" tags within the
        "mutation" tag.
        :param mutation_eventparams: The "name" attribute of "eventparam" tags within
        the "mutation" tag.
        :param fields: A mapping of field names to values.
        :param values: A mapping of value names to values.
        :param statements: A mapping of statement names to values.
        :param collapsed: Whether this block is collapsed.
        :param next: The chained next block.
        """
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
        self.collapsed = collapsed
        self.next = next
        self.id = id
        if id is None:
            self.id = str(type_(self).NEXT_ID)
            type_(self).NEXT_ID += 1

    def _to_xml(self):
        kws = {}
        if self.collapsed:
            kws['collapsed'] = 'true'
        block = E(
            'block', type=self.type, id=self.id, x=str(self.x), y=str(self.y), **kws
        )
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
        """
        Returns the XML representation of the block.
        :return: The XML representation.
        """
        return ET.tostring(self._to_xml()).replace(b'\n', b'&#10;').decode()

    def chain(self, block: 'Block') -> 'Block':
        """
        Chains a block at the end of this block's chain. This means that the block will
        be added right after this block if there is no next block set, otherwise it will
        recurse down the next blocks until it reaches the end.
        :param block: The block to chain.
        :return: `self`
        """
        cur = self
        while cur.next is not None:
            cur = cur.next
        cur.next = block
        return self

    @classmethod
    def _from_xml(cls, xml):
        kwargs = {
            'type': xml.get('type'),
            'x': int(xml.get('x', 0)),
            'y': int(xml.get('y', 0)),
            'id': xml.get('id'),
        }
        if xml.get('collapsed') == 'true':
            kwargs['collapsed'] = True
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
                    elif c.tag.endswith('eventparam'):
                        kwargs.setdefault('mutation_eventparams', []).append(
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
        """
        Create a BlocklyProject from the XML format.
        :param xml: The XML string.
        :return: A created Block.
        """
        return cls._from_xml(ET.fromstring(xml))
