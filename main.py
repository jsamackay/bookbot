from stats import get_num_words
from stats import get_character_count
from stats import sorted_character_count
import sys


def get_book_text(path):
    with open(path) as f:
        return f.read()

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    print("============ BOOKBOT ============")
    book = sys.argv[1]
    print(f"Analyzing book found at {book}")
    text = get_book_text(book)
    numWords = get_num_words(text)
    print("----------- Word Count ----------")
    print(f"Found {numWords} total words")
    charCounts = get_character_count(text)
    sortedCharCounts = sorted_character_count(charCounts)
    print("--------- Character Count -------")
    for char in sortedCharCounts:
        character = char["char"]
        count = char["count"]
        print(f"{character}: {count}")

main()