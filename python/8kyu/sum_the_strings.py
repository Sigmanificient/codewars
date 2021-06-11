def sum_str(a: str, b: str) -> str:
    """https://www.codewars.com/kata/5966e33c4e686b508700002d

    Create a function that takes 2 non negative integers in form of a string as an input, and outputs the sum
    (also as a string)
    """
    return f"{int(f'0{a}') + int(f'0{b}')}"
