// Package strain provides functions for filtering elements from collections.
// The supported collections are []int, [][]int and []string.
package strain

type Ints []int
type Lists [][]int
type Strings []string

func (elements Lists) Keep(test func([]int) bool) Lists {
	var result Lists
	for _, element := range elements {
		if test(element) {
			result = append(result, element)
		}
	}
	return result
}

func (elements Strings) Keep(test func(string) bool) Strings {
	var result Strings
	for _, element := range elements {
		if test(element) {
			result = append(result, element)
		}
	}
	return result
}

func (elements Ints) Keep(test func(int) bool) Ints {
	var result Ints
	for _, element := range elements {
		if test(element) {
			result = append(result, element)
		}
	}
	return result
}

func (elements Ints) Discard(test func(int) bool) Ints {
	return elements.Keep(func(i int) bool { return !test(i) })
}
