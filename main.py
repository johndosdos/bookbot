def print_report(word_count: int, freq_dict: dict[str, int]):
    print("\n")
    print("----------------File Report----------------")
    print(f"There are {word_count} words found in this book.")
    print("\n")
    for item in freq_dict:
        print(f"The character '{item}' is repeated {freq_dict[item]} times.")
    print("----------------End----------------")
    print("\n")


def sort_freq_dict(freq_dict: dict[str, int]) -> dict[str, int]:
    sorted_dict = dict(
        sorted(freq_dict.items(), key=lambda item: item[1], reverse=True)
    )

    return sorted_dict


def get_book_letter_freq(book: str) -> dict[str, int]:
    letter_freq_dict: dict[str, int] = {}
    char_list = book.lower()

    for char in char_list:
        if char.isalpha():
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
    letter_freq_dict = get_book_letter_freq(book)
    sorted_freq_dict = sort_freq_dict(letter_freq_dict)

    print_report(word_count, sorted_freq_dict)


main()
