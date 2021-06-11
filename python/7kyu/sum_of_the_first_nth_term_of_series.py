def series_sum(n: int) -> str:
    """https://www.codewars.com/kata/555eded1ad94b00403000071

    Task:
    Your task is to write a function which returns the sum of following series upto nth term(parameter).
    Series: 1 + 1/4 + 1/7 + 1/10 + 1/13 + 1/16 +...

    Rules:
    - You need to round the answer to 2 decimal places and return it as String.
    - If the given value is 0 then it should return 0.00
    - You will only be given Natural Numbers as arguments.
    """
    return f"{sum(1/(1 + 3 * x) for x in range(n)):.2f}"
