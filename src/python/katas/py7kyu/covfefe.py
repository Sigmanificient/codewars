"""Kata url: https://www.codewars.com/kata/592fd8f752ee71ac7e00008a."""


def covfefe(s: str) -> str:
    return (
        s.replace("coverage", "covfefe")
        if "coverage" in s else f"{s} covfefe"
    )


def test_covfefe():
    assert covfefe("coverage") == "covfefe"
    assert covfefe("coverage coverage") == "covfefe covfefe"
    assert covfefe("nothing") == "nothing covfefe"
    assert covfefe("double space ") == "double space  covfefe"
    assert covfefe("covfefe") == "covfefe covfefe"
