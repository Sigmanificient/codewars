"""Kata url: https://www.codewars.com/kata/56ef9790740d30a7ff000199."""

from __future__ import annotations
from collections import defaultdict
from typing import DefaultDict, Optional, List, TypeVar, cast

T = TypeVar('T')
NodeLevels = DefaultDict[int, List[T]]


class Node[T]:
    def __init__(self, data: T, child_nodes: Optional[List[Node]] = None):
        self.data: T = data
        self.child_nodes: List[Node] = child_nodes or []


def tree_to_list(
    node: Node[T],
    out: Optional[NodeLevels] = None,
    level: int = 0
) -> List[T]:
    if not node:
        return []

    if out is None:
        out  = defaultdict(list)

    out[level].append(node.data)

    for child_node in node.child_nodes:
        tree_to_list(child_node, out, level + 1)

    if not level:
        return [v for v in cast(List[T], out.values())]
    return []


def test_tree_to_list():
    assert tree_to_list(
        Node(1, [Node(2, [Node(3), Node(4), Node(5)]), Node(3, [Node(7)])])
    ) == [1, 2, 3, 3, 4, 5, 7]

    assert tree_to_list(
        Node(1, [Node(2, [Node(3), Node(4)]), Node(5, [Node(6)]), Node(7)])
    ) == [1, 2, 5, 7, 3, 4, 6]

    assert tree_to_list(
        Node(
            1, [
                Node('a', [Node('A'), Node('B')]),
                Node('b', [Node('C'), Node('D', [Node(None)])])
            ]
        )
    ) == [1, 'a', 'b', 'A', 'B', 'C', 'D', None]

    assert tree_to_list(
        Node(
            'H', [
                Node('e', [Node('l'), Node('o', [Node('w'), Node('!')])]),
                Node('l')
            ]
        )
    ) == ['H', 'e', 'l', 'l', 'o', 'w', '!']