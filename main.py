
def word_count(text):
    return len(text.split())

def letter_count(text):
    count = {}
    for c in text.lower():
        try:
            count[c] += 1
        except KeyError:
            count[c] = 1
    return count

def ordered_letter_count(text):
    count = []
    for c,n in letter_count(text).items():
        count.append((c,n))
    count.sort(key = lambda x: x[1], reverse = True)
    return count

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

main()

