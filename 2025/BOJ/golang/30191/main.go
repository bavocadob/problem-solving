package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

func main() {
	reader := bufio.NewReader(os.Stdin)

	line, _ := reader.ReadString('\n')
	n, _ := strconv.Atoi(line[:len(line)-1])

	s, _ := reader.ReadString('\n')
	s = s[:len(s)-1]

	var rst []byte

	idx := n - 1
	SCnt, UCnt := 0, 0

	for idx >= 0 {
		ch := s[idx]

		if ch == 'S' && SCnt > 0 {
			SCnt--
			idx--
			rst = append(rst, 'N')
			continue
		}

		if ch == 'U' && UCnt > 0 {
			UCnt--
			idx--
			rst = append(rst, 'N')
			continue
		}

		substr := s[idx-1 : idx+1]
		if substr == "SU" {
			idx -= 2
			rst = append(rst, 'S', 'N', 'N')
		} else if substr == "US" {
			idx -= 2
			rst = append(rst, 'U', 'N', 'N')
		} else if substr == "SS" {
			idx -= 1
			rst = append(rst, 'U', 'N')
			UCnt++
		} else if substr == "UU" {
			idx -= 1
			rst = append(rst, 'S', 'N')
			SCnt++
		}
	}

	fmt.Println(len(rst))
	fmt.Println(string(rst))
}
