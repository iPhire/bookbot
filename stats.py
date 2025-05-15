def get_num_words(text):
    words = text.split()
    word_count = len(words)
    return word_count

def get_num_char(text):
        dictionary = {}
        words = text.lower()
        for c in words:
              if c in dictionary:
                    dictionary[c] = dictionary[c] + 1
              else:
                    dictionary[c] = 1
        return dictionary

def chars_dict_to_sorted_list(text):
    sorted_chars = []

    for char, count in text.items():
        char_info = {"char": char, "num": count}
        sorted_chars.append(char_info)


    sorted_chars.sort(reverse=True, key=lambda dict: dict["num"])

    return sorted_chars