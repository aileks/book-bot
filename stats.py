def get_word_count(text: str) -> int:
    words = text.split()
    return len(words)


def get_char_count(text: str) -> dict[str, int]:
    letters = [char.lower() for char in text if char.isalpha()]
    return {letter: letters.count(letter) for letter in set(letters)}
