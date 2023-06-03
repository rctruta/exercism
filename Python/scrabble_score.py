def is_valid(word):
    """Validate the word given."""
    return len([ch for ch in word if ch < 'A' or ch > 'Z']) == 0

def generate_scrabble_values():
    """
    Letter Values:
    Letter                           Value
    A, E, I, O, U, L, N, R, S, T       1
    D, G                               2
    B, C, M, P                         3
    F, H, V, W, Y                      4
    K                                  5
    J, X                               8
    Q, Z                               10
    """
    values = {letter: score for (letters, score) in {
        'AEILNORSTU': 1, 'DG': 2, 'BCMP': 3,
        'FHVWY': 4, 'K': 5, 'JX': 8, 'QZ': 10
    }.items() for letter in letters}
    return values

def score(word):
    """Given a word, compute the Scrabble score for that word."""
    if len(word) == 0:
        return 0
    word = word.upper()
    if not is_valid(word):
        raise ValueError("Invalid word")
    values = generate_scrabble_values()
    return sum((values[letter] for letter in word))
