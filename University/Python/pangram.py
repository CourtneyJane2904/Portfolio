%run -i ../m269_util

# problem: Given a string, find which letters must be added for it to become a pangram.

import string
from collections import Counter


def missing_letters(text: str) -> str:
    # method one uses set data structures and then difference function
    text_set = set([c for c in text])
    alpha_set = set([c for c in string.ascii_lowercase])
    return "".join(sorted(alpha_set.difference(text_set)))

def missing_letters(text: str) -> str:
    # a counter is used to set up an easy iterative search
    # list comprehensions are also used as they're faster than for loops
    text_counter = Counter(text)
    alpha_set = set([c for c in string.ascii_lowercase])
    return "".join(sorted([ch for ch in alpha_set if text_counter[ch] == 0]))

PANGRAM = 'The quick brown fox jumps over the lazy dog.'

missing_letters_tests = [
    # case,         text,                           missing
    ['pangram',     PANGRAM,                        ''],
    ['no vowels',   'bcd fgh jklmn pqrst vwxyz',    'aeiou'],
    # new tests:
]

test(missing_letters, missing_letters_tests)
