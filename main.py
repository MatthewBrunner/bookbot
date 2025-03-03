def main():
    from stats import get_num_words, get_num_chars, get_list_dict

    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    chars = get_num_chars(text)
    sorted = get_list_dict(chars)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for i in sorted:
        if i.get("char").isalpha():
            print(f"{i.get("char")}: {i.get("count")}")
    print("============= END ===============")


def get_book_text(path):
    with open(path) as f:
        return f.read()


main()
