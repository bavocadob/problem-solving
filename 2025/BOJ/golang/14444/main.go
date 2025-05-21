package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
)

func main() {

	reader := bufio.NewReader(os.Stdin)
	input, _ := reader.ReadString('\n')
	input = strings.TrimSpace(input)

	fmt.Println(manacher(input))
}

func manacher(s string) int {
	t := preprocess(s)
	n := len(t)
	f := make([]int, n)

	center, right := 0, 0
	ans := 0
	for i := 0; i < n; i++ {
		mirror := center*2 - i

		if mirror >= 0 && right > i {
			f[i] = min(f[mirror], right-i)
		}

		for l, r := i-f[i]-1, i+f[i]+1; l >= 0 && r < n && t[l] == t[r]; {
			f[i]++
			l, r = i-f[i]-1, i+f[i]+1
		}

		if i+f[i] > right {
			center = i
			right = i + f[i]
		}

		ans = max(ans, f[i])
	}

	return ans
}

func min(a, b int) int {
	if a < b {
		return a
	}
	return b
}

func max(a, b int) int {
	if a > b {
		return a
	}
	return b
}

func preprocess(s string) string {
	var b strings.Builder
	b.WriteByte('*')
	for _, ch := range s {
		b.WriteRune(ch)
		b.WriteByte('*')
	}
	return b.String()
}
