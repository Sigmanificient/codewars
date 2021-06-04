import os

IMG_BASE_LINK = 'https://github.com/Sigmanificient/Sigmanificient/blob/master/languages_icons/'
CODE_FACTOR = 'https://www.codefactor.io/repository/github/sigmanificient/codewars'
CODE_FACTOR_BTN = f'[![CodeFactor]({CODE_FACTOR}/badge)]({CODE_FACTOR})'

challenges: dict[str:list[str]] = {}
difficulties: dict[str:int] = {i: [] for i in range(1, 9)}

for directory_language in os.listdir('.'):
    if '.' in directory_language:
        continue

    for kyu in os.listdir(directory_language):
        kyu_level = int(kyu[0])

        for file in os.listdir(f'{directory_language}/{kyu}'):
            filename, ext = file.split(".")
            difficulties[kyu_level].append(filename)

            if filename in challenges:
                challenges[filename].append(ext)
            else:
                challenges[filename] = [ext]

stats = '\n'.join(f"{k}kyu : {length}" for k, v in difficulties.items() if (length := len(v)))

with open("readme.md", "w") as f:
    f.write(f"# Codewars {CODE_FACTOR_BTN}\n\n")
    f.write(f"```c\n{stats}\n```\n\n")

    for difficulty, filenames in sorted(difficulties.items()):
        if not filenames:
            continue

        f.write(f"## {difficulty}Kyu :\n\n")

        for filename in filenames:
            for ext in challenges[filename]:
                icons = ' '.join(
                    f'<img src="{IMG_BASE_LINK}{ext}.png" height="20px">'
                    for ext in challenges[filename]
                )

                f.write(f"- `{filename}` | {icons}\n")
