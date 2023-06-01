// Package pangram provides ways to determine if a text is a pangram.
package pangram

import (
	"strings"
)

const alphabetSize = 26

// IsPangram verifies if the input string is a pangram.
// A string is a pangram if it uses all the letters of the alphabet.
// IsPangram iterates over the input string and it stops once it found
// all the letters of the alphabet.
func IsPangram(input string) bool {
	if len(input) < alphabetSize {
		return false
	}
	input = strings.ToLower(input)
	var lettersFound = make([]bool, alphabetSize)
	pos := 0
	countFound := 0
	for _, chr := range input {
		if (chr < 'a') || (chr > 'z') {
			continue
		}
		pos = (alphabetSize - 1) - (int('z') - int(chr))
		if lettersFound[pos] {
			continue
		}
		lettersFound[pos] = true
		countFound++
		if countFound == alphabetSize {
			return true
		}
	}
	return false
}
