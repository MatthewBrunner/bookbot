def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    character_dict = get_num_characters(text)
    print(text)
    print(f"word count is: {num_words}")
    print(get_num_characters)


def get_num_words(text):
    words = text.split()
    return len(words)


def get_num_characters(text):
    character_dict = {}
    text_lower = text.lower()
    for character in text_lower:
        if character not in character_dict:
            character_dict[character] = 1
        character_dict[character] += 1
    return character_dict


def get_book_text(path):
    with open(path) as f:
        return f.read()
    
  
main()


