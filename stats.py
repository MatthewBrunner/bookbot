def get_num_words(text):
    words = text.split()
    return len(words)


def get_num_chars(text):
    char_dict = {}
    lowered_text = text.lower()
    for char in lowered_text:
        if char in char_dict:
            char_dict[char] += 1
        else:
            char_dict.update({char: 1})
    return char_dict


def char_sort(dict):
    def sort_on(dict):
        return dict

    return
