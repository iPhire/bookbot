from stats import get_num_words, get_num_char, chars_dict_to_sorted_list
import sys

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents

def main():
    if len(sys.argv) < 2:
        print('Usage: python3 main.py <path_to_book>')
        sys.exit(1)
    path = sys.argv[1]
    book_text = get_book_text(path)
    print(book_text)
    word_count = get_num_words(book_text)
    print(f'{word_count} words found in the document')
    character_count = get_num_char(book_text)
    for char, count in character_count.items():
        print(f"'{char}': {count}")
    sorted_char = chars_dict_to_sorted_list(character_count)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for char_dict in sorted_char:
        char = char_dict["char"]
        count = char_dict["num"]
        if char.isalpha():
            print(f'{char}: {count}')
    print("============= END ===============")



main()