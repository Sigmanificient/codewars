"""Kata url: https://www.codewars.com/kata/52bef5e3588c56132c0003bc."""
from __future__ import annotations

from collections import defaultdict
from dataclasses import dataclass
from typing import DefaultDict, List, Optional


@dataclass
class Node:
    left: Optional[Node]
    right: Optional[Node]
    value: int


def tree_by_levels(
    node: Optional[Node], d: int = 0, layout: DefaultDict[int, List[int]] = None
):
    if layout is None:
        layout = defaultdict(list)

    if node is None:
        return []

    layout[d].append(node.value)
    tree_by_levels(node.left, d + 1, layout)
    tree_by_levels(node.right, d + 1, layout)

    if not d:
        return sum(layout.values(), [])


def test_tree_by_levels():
    assert tree_by_levels(None) == []
    assert tree_by_levels(
        Node(
            Node(None, Node(None, None, 4), 2),
            Node(Node(None, None, 5), Node(None, None, 6), 3),
            1,
        )
    ) == [1, 2, 3, 4, 5, 6]
