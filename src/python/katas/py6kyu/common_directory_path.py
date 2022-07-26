"""Kata url: https://www.codewars.com/kata/597f334f1fe82a950500004b."""
from typing import List


def get_common_directory_path(pathes: List[str]) -> str:
    out = []

    for parts in zip(*map(lambda x: x.split("/"), pathes)):
        if any(parts[0] != p for p in parts[1:]):
            break

        out.append(parts[0])

    return "/".join(out) + "/" if out else ""


def test_get_common_directory_path():
    assert (
        get_common_directory_path(["/web/images/image1.png", "/web/images/image2.png"])
        == "/web/images/"
    )
    assert (
        get_common_directory_path(
            ["/web/assets/style.css", "/web/scripts/app.js", "home/setting.conf"]
        )
        == ""
    )
    assert (
        get_common_directory_path(["/web/assets/style.css", "/.bin/mocha", "/read.me"])
        == "/"
    )
    assert (
        get_common_directory_path(
            ["/web/favicon.ico", "/web-scripts/dump", "/webalizer/logs"]
        )
        == "/"
    )
