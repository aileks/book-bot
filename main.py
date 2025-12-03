from stats import get_char_count, get_word_count, sort_char_count
import sys


def get_book_text(filepath: str) -> str:
    with open(filepath) as f:
        return f.read()


def main() -> None:
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    contents: str = get_book_text(sys.argv[1])
    num_words = get_word_count(contents)
    num_letters = get_char_count(contents)
    sorted_chars = sort_char_count(num_letters)

    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")

    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")

    print("--------- Character Count -------")
    for count in sorted_chars:
        print(f"{count['letter']}: {count['count']}")

    print("============= END ===============")


if __name__ == "__main__":
    main()
