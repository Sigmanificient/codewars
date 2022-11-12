"""Kata url: https://www.codewars.com/kata/597c684822bc9388f600010f."""
from dataclasses import dataclass


@dataclass
class Dinglemouse:
    first_name: str
    last_name: str

    def get_full_name(self):
        return f'{self.first_name} {self.last_name}'.strip()


def test_dinglemouse():
    assert Dinglemouse('Clint', 'Eastwood').get_full_name() == 'Clint Eastwood'
    assert Dinglemouse('', 'Eastwood').get_full_name() == 'Eastwood'
    assert Dinglemouse('Clint', '').get_full_name() == 'Clint'
    assert Dinglemouse('', '').get_full_name() == ''
