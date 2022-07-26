import re
import os


def check_doc(filename):
    with open(filename) as f:
        first_line = next(f)
        assert re.match(
            r"\"\"\"Kata url: https://www\.codewars\.com/kata/(.+)\.\"\"\"", first_line
        ), f"{filename}: {first_line}"


def test_doc():
    for kyu_lvl in range(3, 9):
        kata_dir = f"src/python/katas/py{kyu_lvl}kyu"
        for filename in os.listdir(kata_dir):
            if not filename.endswith(".py"):
                continue

            if filename.startswith("_"):
                continue

            check_doc(f"{kata_dir}/{filename}")
