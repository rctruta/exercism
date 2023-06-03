from collections import defaultdict
# Determine if a word or phrase is an isogram.
def is_isogram(text) -> bool:
    """
    An isogram (also known as a "nonpattern word") is a word or phrase without a repeating letter, 
    however spaces and hyphens are allowed to appear multiple times.
    """
    if text == "":
        return True
    textList = [letter for letter in text.lower().strip() if letter >= 'a' and letter <= 'z']
    countLetter = defaultdict(int)
    for letter in textList:
        countLetter[letter] += 1
        if countLetter[letter] > 1:
            return False
    return True
