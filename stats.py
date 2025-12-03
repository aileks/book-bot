def get_word_count(text: str) -> int:
    words = text.split()
    return len(words)


def get_char_count(text: str) -> dict[str, int]:
    char_counts = {}

    for char in text:
        if char.isalpha():
            char = char.lower()
            if char in char_counts:
                char_counts[char] += 1
            else:
                char_counts[char] = 1

    return char_counts


def sort_char_count(char_counts: dict[str, int]) -> list:
    sorted_chars = []

    for letter, count in sorted(char_counts.items(), key=lambda x: x[1], reverse=True):
        sorted_chars.append({"letter": letter, "count": count})

    return sorted_chars
