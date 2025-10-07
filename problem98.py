"""Project Euler 98: Anagramic squares

Find the largest square number formed by any member of an anagram pair from the
given word list (input/0098_words.txt).
"""

from pathlib import Path
from collections import defaultdict


def load_words(path='input/0098_words.txt'):
    text = Path(path).read_text().strip()
    # file is a single line of quoted words separated by commas
    words = [w.strip('"') for w in text.split(',')]
    return words


def pattern(s):
    # canonical pattern: assign indices in order of first appearance
    mapping = {}
    pat = []
    next_id = 0
    for ch in s:
        if ch not in mapping:
            mapping[ch] = next_id
            next_id += 1
        pat.append(mapping[ch])
    return tuple(pat)


def all_squares_by_length(max_len):
    squares_by_len = defaultdict(list)
    n = 1
    while True:
        sq = n * n
        l = len(str(sq))
        if l > max_len:
            break
        squares_by_len[l].append(sq)
        n += 1
    return squares_by_len


def solve():
    words = load_words()
    # group words by sorted letters (anagrams)
    anagrams = defaultdict(list)
    max_len = 0
    for w in words:
        anagrams[''.join(sorted(w))].append(w)
        max_len = max(max_len, len(w))

    squares_by_len = all_squares_by_length(max_len)

    # precompute square patterns by length
    square_patterns = defaultdict(list)  # (length, pattern) -> list of squares
    for l, sqs in squares_by_len.items():
        for sq in sqs:
            p = pattern(str(sq))
            square_patterns[(l, p)].append(sq)

    best = 0

    # consider anagram groups with at least 2 words
    for key, group in anagrams.items():
        if len(group) < 2:
            continue
        # consider all pairs
        for i in range(len(group)):
            for j in range(i + 1, len(group)):
                w1 = group[i]
                w2 = group[j]
                l = len(w1)
                p = pattern(w1)
                # candidate squares matching pattern
                for sq in square_patterns.get((l, p), []):
                    s1 = str(sq)
                    # build mapping from letters in w1 to digits
                    mapping = {}
                    used = set()
                    ok = True
                    for ch, digit in zip(w1, s1):
                        if ch in mapping:
                            if mapping[ch] != digit:
                                ok = False
                                break
                        else:
                            if digit in used:
                                ok = False
                                break
                            mapping[ch] = digit
                            used.add(digit)
                    if not ok:
                        continue
                    # leading zero check
                    if mapping[w2[0]] == '0':
                        continue
                    # form mapped number for w2
                    mapped = int(''.join(mapping[ch] for ch in w2))
                    # check if mapped is a perfect square
                    r = int(int(mapped) ** 0.5)
                    if r * r == mapped:
                        best = max(best, sq, mapped)

    return best


if __name__ == '__main__':
    print(solve())
