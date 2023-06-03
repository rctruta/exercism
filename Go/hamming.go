// Package hamming provides a way to compute the hamming
// distance between two strings.
package hamming

import (
	"errors"
)

// Distance calculates the hamming distance between two strings.
func Distance(a, b string) (int, error) {
	runeA := []rune(a)
	runeB := []rune(b)
	if len(runeA) != len(runeB) {
		return 0, errors.New("strings have different lengths")
	}
	dist := 0
	for index, element := range runeA {
		if element != runeB[index] {
			dist++
		}
	}
	return dist, nil
}
