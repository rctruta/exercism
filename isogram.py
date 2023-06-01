from collections import defaultdict

def is_isogram(text) -> bool:
    if text == "":
        return True
    textList = [letter for letter in text.lower().strip() if letter >= 'a' and letter <= 'z']
    countLetter = defaultdict(int)
    for letter in textList:
        countLetter[letter] += 1
        if countLetter[letter] > 1:
            return False
    return True
