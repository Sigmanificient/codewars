"""Kata url: https://www.codewars.com/kata/52a89c2ea8ddc5547a000863."""


class Node:
    def __init__(self):
        self.next = None


def loop_size(node: Node) -> int:
    collected = []
    while node.next not in collected:
        node = node.next
        collected.append(node)

    return len(collected) - collected.index(node.next)


def test_loop_size():
    # Make a short chain with a loop of 3
    node1 = Node()
    node2 = Node()
    node3 = Node()
    node4 = Node()
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node2

    assert loop_size(node1) == 3

    # Make a longer chain with a loop of 29
    nodes = [Node() for _ in range(50)]
    for node, next_node in zip(nodes, nodes[1:]):
        node.next = next_node
    nodes[49].next = nodes[21]
    assert loop_size(nodes[0]) == 29
