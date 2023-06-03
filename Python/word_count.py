from collections import defaultdict
from re import split

def normalize_word(word):
    return word.strip("'")

def count_words(sentence):
    """Count how many times each word occurs in a subtitle of a drama."""
    cnt = defaultdict(int)
    words = [normalize_word(word) for word in  split(r"[^a-z0-9']+", sentence.lower())]
    for word in words:
        cnt[word] += 1
    cnt.pop('', None) # remove the empty entries
    return cnt

