// Package collatzconjecture provides a function for computing the
// length of a Collatz chain.
package collatzconjecture

import (
	"errors"
)

// CollatzConjecture takes an integer and returns the number of steps
// needed to reach 1 from that number. The steps are computed according
// to the Collatz Conjecture.
func CollatzConjecture(n int) (int, error) {
	if n <= 0 {
		return -1, errors.New("collatzconjecture: invalid input")
	}
	if n == 1 {
		return 0, nil
	}
	count := 0
	for {
		if n == 1 {
			return count, nil
		}
		if n%2 == 0 {
			n = n / 2
		} else {
			n = 3*n + 1
		}
		count++
	}
}
