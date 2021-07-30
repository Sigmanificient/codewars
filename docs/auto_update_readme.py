import os
from typing import Dict, List

USER = "Sigmanificient"
REPO_NAME = "Codewars"

SHIELDS = 'https://img.shields.io'
IMG_BASE_LINK = f'https://github.com/{USER}/{REPO_NAME}/blob/master/docs/img/'
PROFILE = f'![Codewars](https://www.codewars.com/users/{USER}/badges/large)'

EXCLUDED = ['docs', '$RECYCLE.BIN', 'LICENSE']

buttons_urls = {
    'Scrutinizer Code Quality':
        f"https://scrutinizer-ci.com/g/{USER}/{REPO_NAME}"
        f"/badges/quality-score.png?b=master",

    'GitHub code size in bytes':
        f"{SHIELDS}/github/languages/code-size/{USER}/{REPO_NAME}",

    'GitHub repo size':
        f"{SHIELDS}/github/repo-size/{USER}/{REPO_NAME}",

    'Lines of code':
        f"{SHIELDS}/tokei/lines/github/{USER}/{REPO_NAME}",

    'GitHub last commit':
        f"{SHIELDS}/github/last-commit/{USER}/{REPO_NAME}"
}

buttons = '\n'.join(f'![{k}]({v})' for k, v in buttons_urls.items())


challenges: Dict[str, List[str]] = {}
difficulties: Dict[int, List[int]] = {i: [] for i in range(1, 9)}
counts: Dict[int, int] = {}
total: int = 0

for directory_language in os.listdir('.'):
    if directory_language in EXCLUDED or '.' in directory_language:
        continue

    for kyu in os.listdir(directory_language):
        kyu_level = int(kyu[0])

        for file in os.listdir(f'{directory_language}/{kyu}'):
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

stats = '\n'.join(f"{k}kyu : {v}" for k, v in sorted(counts.items()) if v)

with open("readme.md", "w") as f:
    f.write(f"# Codewars\n\n{buttons}\n\n<br>\n\n{PROFILE}")
    f.write(
        f"\n\n*{sum(counts.values())} solved katas !*\n\n```c\n{stats}\n```\n"
    )

    for difficulty, filenames in sorted(difficulties.items()):
        if not filenames:
            continue

        f.write(
            f"<details>\n"
            f"<summary>\n"
            f"<h2>{difficulty}Kyu</h2>\n"
            f"</summary>\n"
            f"\n"
        )

        for filename in sorted(filenames):
            icons = ' '.join(
                f'<img src="{IMG_BASE_LINK}{ext}.png" height="20px">'
                for ext in challenges[filename]
            )

            f.write(
                f"\n"
                f"\t`{filename.replace('_', ' ').capitalize()}`:\n"
                f"\t{icons}\n"
            )

        f.write('</details>')
