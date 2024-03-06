def get_book_word_count() -> int:
    with open("books/frankenstein.txt") as file:
        file_contents = file.read()
        string_list = file_contents.split()

        return len(string_list)


def main():
    word_count = get_book_word_count()

    return f"Number of words: {word_count} words"


result = main()
print(result)
