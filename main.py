def main():
    import sys
    from stats import get_num_words, get_num_chars, get_list_dict

    arg_count = 0
    for i in sys.argv:
        arg_count += 1
    if arg_count < 2:
        print("Proper usage is: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]
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
