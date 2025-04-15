package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
)

func solve(s string) int {
	doubled := s + s
	sRev := reverse(s)

	if strings.Contains(doubled, sRev) {
		return 1
	}
	return 0
}

func reverse(s string) string {
	runes := []rune(s)
	n := len(runes)
	for i := 0; i < n/2; i++ {
		runes[i], runes[n-1-i] = runes[n-1-i], runes[i]
	}
	return string(runes)
}

func main() {
	reader := bufio.NewReader(os.Stdin)
	input, _ := reader.ReadString('\n')
	s := strings.TrimSpace(input)
	fmt.Println(solve(s))
}
