def get_book_letter_freq(book: str) -> dict[str, int]:
    letter_count_dict: dict[str, int] = {}
    char_list = sorted(book.lower())

    for char in char_list:
        if "a" <= char <= "z":
            letter_count_dict[char] = letter_count_dict.get(char, 0) + 1

    return letter_count_dict


def get_book_word_count(book: str) -> int:
    string_list = book.split()

    return len(string_list)


def open_book():
    with open("books/frankenstein.txt") as file:
        file_contents = file.read()

        return file_contents


def main():
    word_count = get_book_word_count()

    return f"Number of words: {word_count} words"


result = main()
print(result)
