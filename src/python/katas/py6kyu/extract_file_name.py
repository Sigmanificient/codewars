"""Kata url: https://www.codewars.com/kata/597770e98b4b340e5b000071."""
import re

FILE_PATTERN = r"(\d+)_(?P<F>([^\.]+.[^\.]+))"


class FileNameExtractor:
    @staticmethod
    def extract_file_name(dirty_file_name: str) -> str:
        return re.match(FILE_PATTERN, dirty_file_name)["F"]


def test_filename_extractor():
    assert (
        FileNameExtractor.extract_file_name(
            "1231231223123131_FILE_NAME.EXTENSION.OTHEREXTENSION"
        )
        == "FILE_NAME.EXTENSION"
    )

    assert (
        FileNameExtractor.extract_file_name(
            "1_FILE_NAME.EXTENSION.OTHEREXTENSIONadasdassdassds34"
        )
        == "FILE_NAME.EXTENSION"
    )
