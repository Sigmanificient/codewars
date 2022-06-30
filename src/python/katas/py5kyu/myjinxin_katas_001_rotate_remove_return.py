from typing import List


def rotate_and_remove(arr: List[List[int]]) -> int:
    while len(arr) > 1:
        new = [[] for _ in range(len(arr[0]))]

        for line in arr:
            for cx, i in enumerate(line[::-1]):
                new[cx].append(i)

        for line in new:
            line.remove(min(line))
            line.remove(max(line))

        arr = new
    return arr[0][0]


def test_rotate_and_remove():
    assert rotate_and_remove(
        [[3, 5, 8, 4, 2], [1, 9, 2, 3, 8], [4, 6, 7, 2, 2],
         [7, 5, 5, 5, 5], [6, 5, 3, 8, 1]]
    ) == 4

    assert rotate_and_remove(
        [[13, 25, 38, 44, 52], [61, 79, 82, 93, 18], [24, 36, 47, 52, 62],
         [77, 85, 95, 15, 25], [36, 45, 53, 68, 71]]
    ) == 47
