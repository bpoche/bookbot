from pprint import pprint

def book_text_to_string(book_loc):
    with open(book_loc) as f:
        file_contents = f.read()
    return file_contents

def count_words(text):
    words = text.split()
    return len(words)

def sort_on(dict):
    return dict["num"]

def char_occurence(text):
    text_lower = text.lower()
    set_lower = set(text_lower)
    char_occurences=[]
    for character in set_lower:
        if character.isalpha() == False:
            continue
        char_cnt=0
        for character_ in text_lower:
            if character_ == character:
                char_cnt+=1
        char_occurences.append({"name":character,"num":char_cnt})
    char_occurences.sort(reverse=True,key=sort_on)
    return char_occurences

def print_report(book_loc):
    book_str = book_text_to_string(book_loc)
    word_count = count_words(book_str)
    char_counts = char_occurence(book_str)
    print(f"--- Begin report of {book_loc} ---")
    print(f"{word_count} words found in the document\n")
    for char_dict in char_counts:
        print(f"The '{char_dict['name']}' character was found {char_dict['num']} times")
    print("--- End report ---")

book_loc = "books/frankenstein.txt"
print_report(book_loc)