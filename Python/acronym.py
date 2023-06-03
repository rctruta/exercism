from re import split

def abbreviate(words):
    """Convert a phrase to its acronym."""

    if len(words) == 0:
        return words
    words = (word for word in  split(r"[^a-zA-Z']+", words))
    abbreviation = ''
    for word in words:
        abbreviation += word[0].upper()
    return abbreviation    
