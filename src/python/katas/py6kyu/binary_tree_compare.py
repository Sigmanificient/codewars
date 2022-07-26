"""Kata url: https://www.codewars.com/kata/55847fcd3e7dadc9f800005f."""
from typing import Optional


class Node:
    def __init__(self, val, left, right):
        self.val = val
        self.left = left
        self.right = right


def compare(a: Optional[Node], b: Optional[Node]) -> bool:
    if a is None:
        return b is None

    if b is None:
        return False

    return a.val == b.val and compare(a.left, b.left) and compare(a.right, b.right)


def test_compare():
    a_node = Node(1, None, None)
    b_node = Node(1, None, None)
    c_node = Node(2, None, None)

    assert compare(a_node, b_node)
    assert not compare(a_node, c_node)
