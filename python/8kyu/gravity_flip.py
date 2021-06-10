from typing import List


def flip(d: str, a: List[int]) -> List[int]:
    """
    If you've completed this kata already and want a bigger challenge, here's the 3D version

    Bob is bored during his physics lessons so he's built himself a toy box to help pass the time. The box is special
    because it has the ability to change gravity.

    There are some columns of toy cubes in the box arranged in a line. The i-th column contains a_i cubes. At first, the
    gravity in the box is pulling the cubes downwards. When Bob switches the gravity, it begins to pull all the cubes to
    a certain side of the box, d, which can be either 'L' or 'R' (left or right). Below is an example of what a box of
    cubes might look like before and after switching gravity.
    """
    return sorted(a)[::-1 if d == 'L' else 1]
