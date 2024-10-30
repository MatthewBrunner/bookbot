def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = word_count(text)
    chars = char_count(text)
    print(f"{num_words} words were found in {book_path}")
    print(f"{chars}")


def word_count(text):
    words = text.split()
    return len(words)


def get_book_text(path):
    with open(path) as f:
        return f.read()


def char_count(text):
    char_dict = {}
    lowered_text = text.lower()
    for char in lowered_text:
        if char in char_dict:
            char_dict[char] += 1
        else:
            char_dict.update({char: 1})
    return char_dict


main()
