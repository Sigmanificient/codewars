"""Kata url: https://www.codewars.com/kata/57262ca48565846f33001365."""


def reverse_list(node):
    nodes = []
    first_node = node

    while node is not None:
        nodes.append(node)
        node = node.next

    cut = (len(nodes) // 2)
    rev = nodes[::-1][:cut]

    for node_front, node_back in zip(nodes, rev):
        node_back.value, node_front.value = node_front.value, node_back.value
    return first_node
