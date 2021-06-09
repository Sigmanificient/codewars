def iq_test(numbers: str) -> int:
    """
    https://www.codewars.com/kata/552c028c030765286c00007d/

    Bob is preparing to pass IQ test. The most frequent task in this test is to find out which one of the given numbers
    differs from the others. Bob observed that one number usually differs from the others in evenness. Help Bob — to
    check his answers, he needs a program that among the given numbers finds one that is different in evenness, and
    return a position of this number.

    ! Keep in mind that your task is to help Bob solve a real IQ test, which means indexes of the elements start from 1
    (not 0)
    """
    oddness = [x % 2 for x in map(int, numbers.split())]
    return oddness.index(sum(oddness) == 1) + 1
