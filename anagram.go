// Package anagram provides  utilities for checking anagrams of a given
// string against a list of strings. The solution is case-insensitive.
package anagram

import (
	"errors"
	"sort"
	"strings"
)

type sortRunes []rune

func (s sortRunes) Less(i, j int) bool {
	return s[i] < s[j]
}

func (s sortRunes) Swap(i, j int) {
	s[i], s[j] = s[j], s[i]
}

func (s sortRunes) Len() int {
	return len(s)
}

// sortString sorts the characters of a string.
func sortString(s string) string {
	r := []rune(s)
	sort.Sort(sortRunes(r))
	return string(r)
}

// validateInput checks for erroneous input values
func validateInput(s string, list []string) error {
	if len(list) != 0 {
		return nil
	}
	return errors.New("Invalid candidates; expected a string of length > 0")
	//All sorts of erroneous inputs should be addressed here:
	// what happens when s contains whitespaces? Trim or ignore?
}

// isAnagram verifies whether candidate is an anagram of subject.
func isAnagram(subject string, candidate string) bool {
	if len(subject) != len(candidate) {
		return false
	}
	return sortString(strings.ToLower(subject)) == sortString(strings.ToLower(candidate))
}

// Detect returns, from an array of <candidate>s strings, those that are
// anagrams of a given <subject> input string.
func Detect(subject string, candidates []string) []string {
	err := validateInput(subject, candidates)
	if err != nil {
		panic(err)
	}
	if subject == "" {
		return candidates
	}
	result := make([]string, 0)
	for _, candidate := range candidates {
		if isAnagram(subject, candidate) {
			result = append(result, candidate)
		}
	}
	return result
}
