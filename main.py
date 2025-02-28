def main():
    from stats import get_num_words, char_count

    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    chars = char_count(text)
    print(f"{num_words} words were found in the document")
    print(f"{chars}")


def get_book_text(path):
    with open(path) as f:
        return f.read()


main()
