"""Kata url: https://www.codewars.com/kata/56214b6864fe8813f1000019."""
from functools import partial

status = []
funcs = [partial(status.append, i) for i in range(6)]

roll_dice, move, combat, *more = funcs
get_coins, buy_health, print_status = more

# ------------------------------------------------------------------------------
# from preloaded import *

health = 100
position = 0
coins = 0


def main():
    roll_dice()
    move()
    combat()
    get_coins()
    buy_health()
    print_status()


def test_main():
    main()
    assert status == list(range(6))
