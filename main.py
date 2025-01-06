



def print_report(number_of_words, chars_sorted_list):
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{number_of_words} words found in the document")
    print("")

    for item in chars_sorted_list:
        if item["char"].isalpha():
            print(f"The '{item['char']}' character was found {item['num']} times")
    print("--- End report ---")


def sort_on(dict):
    return dict["num"]


def chars_dict_to_sorted_list(chars_dict):
    sorted_list = []
    for char in chars_dict:
        sorted_list.append({"char": char, "num":chars_dict[char]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list


def get_num_char_dict(text):
    lower_text = text.lower()
    chars = {}
    for char in lower_text:
        if char in chars:
            chars[char] += 1
        else:
            chars[char] = 1
    return chars


def get_num_words(text):
    words = text.split()
    return len(words)


def get_book_text(path):
    with open(path) as f:
        return f.read()


def main():
    text = get_book_text("books/frankenstein.txt")
    print_report(get_num_words(text), chars_dict_to_sorted_list(get_num_char_dict(text)))



main()

