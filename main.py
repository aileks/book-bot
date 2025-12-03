from stats import get_char_count, get_word_count


def get_book_text(filepath: str) -> str:
    with open(filepath) as f:
        return f.read()


def main() -> None:
    contents: str = get_book_text("./books/frankenstein.txt")
    num_words = get_word_count(contents)
    num_letters = get_char_count(contents)
    print(f"Found {num_words} total words")
    print(num_letters)


if __name__ == "__main__":
    main()
