def get_num_words(text):
    return len(text.split())

def get_character_count(text):
    characterCounts = {}

    for char in text:
        if char.lower() not in characterCounts:
            characterCounts[char.lower()] = 0

        characterCounts[char.lower()] += 1

    return characterCounts

def sort_on(dict):
    return dict["count"]

def sorted_character_count(characterCounts):
    chars = []
    for char in characterCounts:
        if not char.isalpha():
            continue
        chars.append({"char": char, "count": characterCounts[char]})

    chars.sort(reverse=True, key=sort_on)

    return chars