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


def get_list_dict(dict):
    list_of_dicts = []

    def sort_on(dict):
        return dict["count"]

    for c in dict:
        temp_dict = {"char": c, "count": dict.get(c)}
        list_of_dicts.append(temp_dict)
    list_of_dicts.sort(reverse=True, key=sort_on)
    return list_of_dicts
