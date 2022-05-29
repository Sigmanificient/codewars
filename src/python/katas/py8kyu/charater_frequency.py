from typing import Dict


def char_freq(message: str) -> Dict[str, int]:
    return {
        char: message.count(char) for char in message
    }
