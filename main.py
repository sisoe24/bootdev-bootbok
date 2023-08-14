import os

path_to_file = os.path.join(os.path.dirname(__file__), 'books', 'frankenstein.txt')

def count_words(text: str) -> int:
    return len(text.split())

def count_letters(text: str) -> dict[str, int]:
    letters = {}
    for letter in text.lower():
        if not letter.isalpha():
            continue

        if letter in letters:
            letters[letter] += 1
        else:
            letters[letter] = 1
    return letters

def print_report(words: int, letters: dict[str, int]) -> None:

    print('-- REPORT START --')

    print("words:", words)
    print("letters:")
    for letter, count in sorted(letters.items()):
        print(f"{letter}: {count}")

    print('-- REPORT END --')

with open(path_to_file, 'r') as f:
    text = f.read()

    words = count_words(text)
    letters = count_letters(text)

    print_report(words, letters)
