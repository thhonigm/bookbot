
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
        count.append({"char": c, "num": n})
    count.sort(key = lambda x: x["num"], reverse = True)
    return count

