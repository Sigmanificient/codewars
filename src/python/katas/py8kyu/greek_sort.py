"""Kata url: https://www.codewars.com/kata/56bc1acf66a2abc891000561."""

from typing import Tuple

greek_alphabet: Tuple[str, ...] = (
    'alpha', 'beta', 'gamma', 'delta', 'epsilon', 'zeta',
    'eta', 'theta', 'iota', 'kappa', 'lambda', 'mu',
    'nu', 'xi', 'omicron', 'pi', 'rho', 'sigma',
    'tau', 'upsilon', 'phi', 'chi', 'psi', 'omega'
)


def greek_comparator(lhs: str, rhs: str) -> int:
    return greek_alphabet.index(lhs) - greek_alphabet.index(rhs)


def test_greek_comparator():
    assert greek_comparator('alpha', 'beta') < 0
    assert greek_comparator('psi', 'psi') == 0
    assert greek_comparator('upsilon', 'rho') > 0
