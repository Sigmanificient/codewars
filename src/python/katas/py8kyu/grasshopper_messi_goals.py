"""Kata url: https://www.codewars.com/kata/55ca77fa094a2af31f00002a."""

la_liga_goals: int = 43
champions_league_goals: int = 10
copa_del_rey_goals: int = 5

total_goals = la_liga_goals + champions_league_goals + copa_del_rey_goals


def test_solution():
    assert la_liga_goals == 43
    assert champions_league_goals == 10
    assert copa_del_rey_goals == 5

    assert total_goals == 58
