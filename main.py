import sys
from stats import word_count, ordered_letter_count

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    path = sys.argv[1]
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
