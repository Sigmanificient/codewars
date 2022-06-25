from typing import Optional


class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


def stringify(node: Optional[Node]) -> str:
    if node is None:
        return 'None'

    return f"{node.data} -> {stringify(node.next)}"


def test_stringify():
    assert stringify(None) == 'None'

    assert stringify(
        Node(0, Node(1, Node(2, Node(3))))
    ) == '0 -> 1 -> 2 -> 3 -> None'

    assert stringify(
        Node(0, Node(1, Node(4, Node(9, Node(16)))))
    ) == '0 -> 1 -> 4 -> 9 -> 16 -> None'
