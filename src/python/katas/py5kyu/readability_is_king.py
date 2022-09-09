"""Kata url: https://www.codewars.com/kata/52b2cf1386b31630870005d4."""

VOWELS = set('aeiou')
PUNCTUATION = set('.!?')


def get_syllables(word):
    syllables = 0
    previous = False

    for item in word:
        if item not in VOWELS:
            previous = False
            continue

        if previous:
            continue

        syllables += 1
        previous = True

    return syllables


def parse_text(text):
    words = ['']
    nb_sentences = 0
    i = 0

    for char in text:
        if char == ' ':
            words.append('')
            i += 1
            continue

        if char in PUNCTUATION:
            nb_sentences += 1
            continue

        words[-1] += char

    return nb_sentences, words


def flesch_kincaid(text):
    nb_sentences, words = parse_text(text.lower())

    nb_words = len(words)
    avg_words = nb_words / nb_sentences
    avg_syllables = sum(get_syllables(w) for w in words) / nb_words

    return round(
        (0.39 * avg_words) + (11.8 * avg_syllables) - 15.59,
        2
    )


def test_get_syllables():
    assert get_syllables('a') == 1
    assert get_syllables('deal') == 1
    assert get_syllables('tea') == 1
    assert get_syllables('courage') == 3
    assert get_syllables('paragraph') == 3
    assert get_syllables('floccaucinihilipilification') == 11


def test_parse_text():
    assert parse_text("The turtle is leaving.") == (
        1, ['The', 'turtle', 'is', 'leaving']
    )

    assert parse_text("Oh no! The lemming is falling.") == (
        2, ['Oh', 'no', 'The', 'lemming', 'is', 'falling']
    )


def test_flesch_kincaid():
    assert flesch_kincaid("The turtle is leaving.") == 3.67
    assert flesch_kincaid("A good book is hard to find.") == -1.06
    assert flesch_kincaid("To be or not to be. That is the question.") == -0.66
    assert flesch_kincaid("Oh no! The lemming is falling.") == 1.31
    assert flesch_kincaid(
        "Do not cut your fingers as your katana is getting sharper! Be gentle."
    ) == 4.19
