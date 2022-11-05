"""Kata url: https://www.codewars.com/kata/55849d76acd73f6cc4000087."""


def player_rank_up(pts):
    if pts < 100:
        return False

    return (
        "Well done! You have advanced to the qualifying stage."
        " Win 2 out of your next 3 games to rank up."
    )


def test_player_rank_up():
    assert not player_rank_up(64)
    assert player_rank_up(180) == (
        "Well done! You have advanced to the qualifying stage."
        " Win 2 out of your next 3 games to rank up."
    )
