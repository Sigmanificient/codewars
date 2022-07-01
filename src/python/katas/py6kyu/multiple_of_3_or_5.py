def solution(number: int) -> int:
    return sum(
        n for n in range(number)
        if not n % 3 or not n % 5
    )


def test_solution():
    assert solution(4) == 3
    assert solution(6) == 8
    assert solution(16) == 60
    assert solution(3) == 0
    assert solution(5) == 3
    assert solution(15) == 45
    assert solution(0) == 0
    assert solution(-1) == 0
    assert solution(10) == 23
    assert solution(20) == 78
    assert solution(200) == 9168
