// Package secret provides a way to decode a secret handshake code.
package secret

const (
	wink uint = 1 << iota
	doubleBlink
	closeYourEyes
	jump
)

var secretCode = map[uint]string{
	wink:          "wink",
	doubleBlink:   "double blink",
	closeYourEyes: "close your eyes",
	jump:          "jump",
}

// Handshake converts a given binary number into a series of actions.
func Handshake(code uint) []string {
	decodedMessage := []string{}
	shouldReverse := ((1 << len(secretCode)) & code) != 0
	for i := 0; i < len(secretCode); i++ {
		if shouldReverse {
			secret, ok := secretCode[(1<<(len(secretCode)-1-i))&code]
			if ok {
				decodedMessage = append(decodedMessage, secret)
			}
		} else {
			secret, ok := secretCode[(1<<i)&code]
			if ok {
				decodedMessage = append(decodedMessage, secret)
			}
		}
	}
	return decodedMessage
}
