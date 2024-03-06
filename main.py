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
