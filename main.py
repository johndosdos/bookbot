def get_book_letter_freq(book: str) -> dict[str, int]:
    letter_freq_dict: dict[str, int] = {}
    char_list = sorted(book.lower())

    for char in char_list:
        if "a" <= char <= "z":
            letter_freq_dict[char] = letter_freq_dict.get(char, 0) + 1

    return letter_freq_dict


def get_book_word_count(book: str) -> int:
    string_list = book.split()

    return len(string_list)


def open_book() -> str:
    with open("books/frankenstein.txt") as file:
        file_contents = file.read()

        return file_contents


def main():
    book = open_book()
    word_count = get_book_word_count(book)
    letter_count = get_book_letter_freq(book)

    print("\n\n----------------------------------")
    print(f"Number of words: {word_count} words\n")
    print(f"Frequency of letters:\n{letter_count}")
    print("----------------------------------\n\n")


main()
