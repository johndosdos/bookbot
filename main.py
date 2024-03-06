def print_report(word_count: int, letter_freq: dict[str, int]):
    print("\n")
    print("----------------File Report----------------")
    print(f"There are {word_count} words found in this book.")
    print("\n")
    for item in letter_freq:
        print(f"The character '{item}' is repeated {letter_freq[item]} times.")
    print("----------------End----------------")
    print("\n")


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

    print_report(word_count, letter_count)


main()
