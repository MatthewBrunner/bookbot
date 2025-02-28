def main():
    from stats import get_num_words, get_num_chars

    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    chars = get_num_chars(text)
    print(f"{num_words} words found in the document")
    print(f"{chars}")


def get_book_text(path):
    with open(path) as f:
        return f.read()


main()
