def get_book_text(book_path) -> str:
    with open(book_path, "r") as book:
        book_text = book.read()
        return book_text


def get_word_count(book_text) -> int:
    number_of_words = len(book_text.split())
    return number_of_words


def get_char_dict(text: str):
    chars = {}
    for c in text.lower():
        if c in chars.keys():
            chars[c] += 1
        else:
            chars[c] = 1
    return chars


def sort_dict(dict):
    return dict["num"]


def convert_to_list(char_dict):
    dict_list = []
    for key in char_dict:
        dict_list.append({"char": key, "num": char_dict[key]})
    dict_list.sort(reverse=True, key=sort_dict)
    return dict_list


def create_report(book_path: str, number_of_words: int, chars_in_list: list):
    print(f"--- Begin report of {book_path} ---")
    print(f"{number_of_words} words are in the document")
    print()

    for item in chars_in_list:
        if item["char"].isalpha():
            print(f"The '{item['char']}' character was found {item['num']} times")

    print("--- End report ---")


def main():
    book_path = "./books/frankenstein.txt"

    book_text = get_book_text(book_path)
    number_of_words = get_word_count(book_text)
    chars_in_book = get_char_dict(book_text)
    chars_in_list = convert_to_list(chars_in_book)

    create_report(book_path, number_of_words, chars_in_list)


if __name__ == "__main__":
    main()
