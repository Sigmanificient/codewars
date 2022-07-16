def row_sum_odd_numbers(n: int) -> int:
    odd = sum(range(n)) * 2 + 1
    return sum(range(odd, odd + (n * 2), 2))


def test_row_sum_odd_numbers():
    assert row_sum_odd_numbers(1) == 1
    assert row_sum_odd_numbers(2) == 8
    assert row_sum_odd_numbers(13) == 2197
    assert row_sum_odd_numbers(19) == 6859
    assert row_sum_odd_numbers(41) == 68921
