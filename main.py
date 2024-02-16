def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    character_dict = get_char_dict(text)
    list_of_dicts = dict_to_list_dict(character_dict)
    list_of_dicts.sort(reverse=True, key=sort_on)
    print("--- Begin report of books/frankenstein.txt ---")
    print()
    print(f"Word count is: {num_words}.")
    print()
    for dict in list_of_dicts:
        print(f"The character {dict['name']} was found {dict['num']} times.")
    print()
    print("--- End report ---")

def get_num_words(text):
    words = text.split()
    return len(words)


def get_char_dict(text):
    char_d = {}
    text_lower = text.lower()
    for character in text_lower:
        if character in char_d:
            char_d[character] += 1
        else:
            char_d[character] = 1
    return char_d

def get_book_text(path):
    with open(path) as f:
        return f.read()

def dict_to_list_dict(dict):
   list_dict = []
   for char in dict:
       if char.isalpha():
           new_dict = {'name': char, 'num': dict[char]}
           list_dict.append(new_dict)
   return list_dict

def sort_on(dict):
    return dict["num"]

main()
