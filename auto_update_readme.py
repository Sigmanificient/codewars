import os

SHIELD = 'https://img.shields.io'
REPO_NAME = 'Sigmanificient/codewars'

IMG_BASE_LINK = 'https://github.com/Sigmanificient/Sigmanificient/blob/master/languages_icons/'

buttons = '\n'.join((
    f'![GitHub code size in bytes]({SHIELD}/github/languages/code-size/{REPO_NAME})',
    f'![GitHub repo size]({SHIELD}/github/repo-size/{REPO_NAME})',
    f'![Lines of code]({SHIELD}/tokei/lines/github/{REPO_NAME})',
    f'![GitHub last commit]({SHIELD}/github/last-commit/{REPO_NAME})'
))

challenges: dict[str:list[str]] = {}
difficulties: dict[str:int] = {i: [] for i in range(1, 9)}

for directory_language in os.listdir('.'):
    if '.' in directory_language:
        continue

    for kyu in os.listdir(directory_language):
        kyu_level = int(kyu[0])

        for file in os.listdir(f'{directory_language}/{kyu}'):
            filename, ext = file.split(".")

            if filename in challenges:
                challenges[filename].append(ext)
            else:
                difficulties[kyu_level].append(filename)
                challenges[filename] = [ext]

stats = '\n'.join(f"{k}kyu : {length}" for k, v in difficulties.items() if (length := len(v)))

with open("readme.md", "w") as f:
    f.write(f"# Codewars\n\n{buttons}\n```c\n{stats}\n```\n\n")

    for difficulty, filenames in sorted(difficulties.items()):
        if not filenames:
            continue

        f.write(f"## {difficulty}Kyu\n\n")

        for filename in sorted(filenames):
            icons = ' '.join(
                f'<img src="{IMG_BASE_LINK}{ext}.png" height="20px">' for ext in challenges[filename]
            )

            f.write(f"*  `{filename.replace('_', ' ').capitalize()}` |\n  {icons}\n\n")
