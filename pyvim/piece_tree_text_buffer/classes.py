from dataclasses import dataclass
from enum import Enum
from typing import List

@dataclass
class PieceTable:
    original: str
    added: str
    nodes: List[Node]

@dataclass
class Node:
    type: NodeType
    start: int
    length: int

class NodeType(Enum):
    Original = False
    Added = False