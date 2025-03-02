import os
import sys

from stats import count_words, count_letters

ROOT = os.path.dirname(__file__)

_, *args = sys.argv

def main(path: str):
    print('=' * 10, 'BOOKBOOT', '=' * 10)

    print(f'Analyzing book found at {path}...')
    print('-' * 10, 'Word Count', '-' * 10)

    with open(path) as f:
        text = f.read()

        words = count_words(text)
        print(f'Found {words} total words')

        print('-' * 10, 'Character Count', '-' * 10)
        letters = count_letters(text)
        for letter, count in sorted(letters.items()):
            print(f'{letter}: {count}')

    print('=' * 10, 'END', '=' * 10)


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Usage: python3 main.py <path_to_book>', file=sys.stderr)
        sys.exit(1)
    main(sys.argv[1])

