import os
from typing import Dict, List

USER = "Sigmanificient"
REPO_NAME = "Codewars"

SHIELDS = "https://img.shields.io"
PROFILE = f"![Codewars](https://www.codewars.com/users/{USER}/badges/large)"
COVERAGE = f"https://codecov.io/gh/{USER}/{REPO_NAME}/branch/master/graph/badge.svg?token=0MNNDL5VSF"


EXCLUDED = [
    "__pycache__",
]

buttons_urls = {
    "GitHub code size in bytes": f"{SHIELDS}/github/languages/code-size/{USER}/{REPO_NAME}",
    "GitHub repo size": f"{SHIELDS}/github/repo-size/{USER}/{REPO_NAME}",
    "Lines of code": f"{SHIELDS}/tokei/lines/github/{USER}/{REPO_NAME}",
    "GitHub last commit": f"{SHIELDS}/github/last-commit/{USER}/{REPO_NAME}",
    "Codecov": COVERAGE,
}

buttons = "\n".join(f"![{k}]({v})" for k, v in buttons_urls.items())


challenges: Dict[str, List[str]] = {}
difficulties: Dict[int, List[str]] = {i: [] for i in range(9)}
counts: Dict[int, int] = {}
total: int = 0

for directory_language in os.listdir("src/"):
    if directory_language in EXCLUDED or "." in directory_language:
        continue

    for kyu in os.listdir(f"src/{directory_language}/katas"):
        if "_" in kyu or "test" in kyu:
            continue

        kyu_level = int("".join(c for c in kyu if c.isdigit()) or 0)

        for file in os.listdir(f"src/{directory_language}/katas/{kyu}"):
            if file.count(".") != 1:
                continue

            if "__" in file:
                continue

            filename, ext = file.split(".")

            if kyu_level not in counts:
                counts[kyu_level] = 0

            if filename in challenges:
                challenges[filename].append(ext)
            else:
                difficulties[kyu_level].append(filename)
                challenges[filename] = [ext]

            counts[kyu_level] += 1
            total += 1

stats = "\n".join(
    f"{k}kyu : {v}" if k else f"beta : {v}" for k, v in sorted(counts.items()) if v
)

with open("docs/readme.md", "w") as f:
    f.write(f"# Codewars\n\n{buttons}\n\n<br>\n\n{PROFILE}")
    f.write(f"\n\n*{sum(counts.values())} solved katas !*\n\n```c\n{stats}\n```\n")

    for difficulty, filenames in sorted(difficulties.items()):
        if not filenames:
            continue

        f.write(
            "\n"
            f"<h2>{difficulty}Kyu</h2>\n"
            "<details>\n"
            "\t<summary>\n"
            f"\t\t<i>views solved {difficulty} kyu</i>\n"
            "\t</summary>\n"
        )

        for filename in sorted(filenames):
            icons = " ".join(
                f'<img src="img/{ext}.png" height="20px">'
                for ext in challenges[filename]
            )

            clean_filename = filename.replace('_', ' ').capitalize()
            f.write(f"\n" f"`{clean_filename}`:\n"{icons}\n")

        f.write("</details>\n")