from dataclasses import dataclass, field
from typing import List

@dataclass
class Node:
    bufferIndex: int
    start: BufferPosition
    length: BufferPosition
    lineStarts: List[int]

    left_subtree_length: int
    left_subtree_lfcnt: int
    left: Node
    right: Node
    parent: Node

@dataclass
class PieceTable:
    buffers: List[str]
    rootNode: Node

@dataclass
class Buffer:
    value: str
    lineStarts: List[int]

@dataclass
class BufferPosition:
    index: int # index in Buffer.lineStarts
    remainder: int