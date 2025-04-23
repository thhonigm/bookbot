from stats import word_count, letter_count

def main1():
    path ="books/frankenstein.txt"
    with open(path) as f:
        file_contents = f.read()
    print(f"{word_count(file_contents)} words found in the document")
    print(letter_count(file_contents))

def main():
    path ="books/frankenstein.txt"
    with open(path) as f:
        file_contents = f.read()

    print(f"--- Begin report of {path} ---")
    print(f"{word_count(file_contents)} words found in the document")
    print()
    for c,n in ordered_letter_count(file_contents):
        if c.isalpha():
            print(f"The '{c}' character was found {n} times")
    print(f"--- End report ---")


main1()
