
def count_words(text: str) -> int:
    return len(text.split())

def count_letters(text: str) -> dict[str, int]:
    letters: dict[str, int] = {}
    for letter in text.lower():
        if not letter.isalpha():
            continue

        if letter in letters:
            letters[letter] += 1
        else:
            letters[letter] = 1
    return letters
