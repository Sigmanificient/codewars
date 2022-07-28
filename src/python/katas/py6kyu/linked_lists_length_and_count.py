from __future__ import annotations

from dataclasses import dataclass
from typing import Optional


@dataclass
class Node:
    data: int
    next: Optional[Node] = None


def length(node: Node) -> int:
    if node is None:
        return 0

    t = 1
    while node.next:
        print(node.data)
        node = node.next
        t += 1
    return t


def count(node: Node, data: int) -> int:
    if node is None:
        return 0

    t = 0
    while node:
        if node.data == data:
            t += 1

        node = node.next
    return t


def test_count():
    assert count(Node(1), 1) == 1
    assert count(Node(1), 2) == 0

    n = Node(1, Node(2, Node(1, Node(2, Node(1, Node(2, Node(1, Node(2))))))))
    assert count(n, 1) == 4


def test_length():
    assert length(Node(1)) == 1
    assert length(Node(1, Node(2))) == 2
    assert length(Node(1, Node(2, Node(3)))) == 3
    assert length(Node(1, Node(2, Node(3, Node(4))))) == 4
