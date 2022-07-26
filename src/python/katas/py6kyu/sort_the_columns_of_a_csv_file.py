"""Kata url: https://www.codewars.com/kata/57f7f71a7b992e699400013f."""
from typing import Dict, List


def sort_csv_columns(csv_file_content: str) -> str:
    lines = csv_file_content.splitlines()
    headers = lines[0].split(";")
    csv_content: Dict[str, List[str]] = {field: [] for field in headers}

    for line in lines[1:]:
        v_fields = line.split(";")

        for v_field, h_field in zip(v_fields, headers):
            csv_content[h_field].append(v_field)

    sorted_header = sorted(headers, key=str.lower)
    return (
        ";".join(sorted_header)
        + "\n"
        + "\n".join(
            ";".join(csv_content[h][i] for h in sorted_header)
            for i in range(len(lines) - 1)
        )
    )


def test_sort_csv_columns():
    assert sort_csv_columns(
        "myjinxin2015;raulbc777;smile67;Dentzil;SteffenVogel_79\n"
        "17945;10091;10088;3907;10132\n"
        "2;12;13;48;11"
    ) == (
        "Dentzil;myjinxin2015;raulbc777;smile67;SteffenVogel_79\n"
        "3907;17945;10091;10088;10132\n"
        "48;2;12;13;11"
    )

    assert sort_csv_columns(
        "Captain America;Hulk;IronMan;Thor\n"
        "honorably;angry;arrogant;divine\n"
        "shield;greenhorn;armor;hammer\n"
        "Steven;Bruce;Tony;Thor"
    ) == (
        "Captain America;Hulk;IronMan;Thor\n"
        "honorably;angry;arrogant;divine\n"
        "shield;greenhorn;armor;hammer\n"
        "Steven;Bruce;Tony;Thor"
    )
