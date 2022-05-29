"""Kata url: https://www.codewars.com/kata/54147087d5c2ebe4f1000805."""


from typing import Any, Callable


def _if(_bool: bool, func1: Callable, func2: Callable) -> Any:
    return (func1 if _bool else func2)()
