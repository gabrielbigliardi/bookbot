def main():
    book_path = "books/frankenstein.txt"
    text = open_file(book_path)
    num_words = get_num_words(text)
    num_letters = count_letters(text)
    chars_sorted_list = chars_dict_to_sorted_list(num_letters)

    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document")
    print()

    for item in chars_sorted_list:
        if not item["char"].isalpha():
            continue
        print(f"The '{item['char']}' character was found {item['num']} times")

    print("--- End report ---")

def get_num_words(text):
    words = text.split()
    return len(words)

def sort_on(d):
    return d["num"]

def count_letters(text):
    counter = {}
    for letter in text:
        letter = letter.lower()
        if letter in counter:
            counter[letter] += 1
        else:
            counter[letter] = 1    
    return counter

def chars_dict_to_sorted_list(num_chars_dict):
    sorted_list = []
    for ch in num_chars_dict:
        sorted_list.append({"char": ch, "num": num_chars_dict[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list    

def open_file(path):
    with open (path) as f:
        return f.read()

main()
