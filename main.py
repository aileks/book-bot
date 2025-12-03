def get_book_text(filepath: str) -> str:
    with open(filepath) as f:
        return f.read()


def main() -> None:
    contents: str = get_book_text("./books/frankenstein.txt")
    print(contents)


if __name__ == "__main__":
    main()
