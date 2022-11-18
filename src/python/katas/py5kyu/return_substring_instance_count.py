"""Kata url: https://www.codewars.com/kata/52190daefe9c702a460003dd."""


def search_substr(text, search_text, allow_overlap=True):
    if not text or not search_text:
        return 0

    i = count = 0
    s_len = len(search_text)
    t_len = len(text) - s_len

    while i <= t_len:
        if text[i: i + s_len] == search_text:
            count += 1

            if not allow_overlap:
                i += (s_len - 1)

        i += 1

    return count


def test_search_substr():
    assert search_substr('aa_bb_cc_dd_bb_e', 'bb') == 2
    assert search_substr('aaabbbcccc', 'bbb') == 1
    assert search_substr('aaacccbbbcccc', 'cc') == 5
    assert search_substr('aaa', 'aa') == 2
    assert search_substr('aaa', 'aa', False) == 1
    assert search_substr('aaabbbaaa', 'bb', False) == 1
    assert search_substr('a', '') == 0
    assert search_substr('', 'a') == 0
    assert search_substr('', '') == 0
    assert search_substr('', '', False) == 0
