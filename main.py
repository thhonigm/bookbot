from stats import word_count, ordered_letter_count

def main():
    path ="books/frankenstein.txt"
    with open(path) as f:
        file_contents = f.read()

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count(file_contents)} total words")
    print("--------- Character Count -------")
    for lc in ordered_letter_count(file_contents):
        if lc["char"].isalpha():
            print(f"{lc["char"]}: {lc["num"]}")
    print("============= END ===============")


main()
