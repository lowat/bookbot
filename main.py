def main():
    path = "books/frankenstein.txt"
    with open(path) as f:
        file_contents = f.read()
        words = file_contents.split()
        print(f"--- Begin report of {path} ---")
        print(f"{len(words)} words found in the document")
        display_letter_counts(words)
        print("--- End report ---")

def construct_letter_dict():
    dict = {}
    library = 'abcdefghijklmnopqrstuvwxyz'
    for l in library:
        dict[l] = 0
    return dict

def count_letters(words):
    dict = construct_letter_dict()
    for word in words:
        for c in word:
            lower_c = c.lower()
            if lower_c in dict:
                dict[lower_c] += 1
    return dict

def display_letter_counts(words):
    dict = count_letters(words)
    sorted_pairs = sorted(dict.items(), key = lambda x:x[1], reverse = True)
    for k,v in sorted_pairs:
        print(f"The '{k}' character was found {v} times")

main()