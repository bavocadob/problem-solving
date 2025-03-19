package main

import (
	"bufio"
	"fmt"
	"os"
	"sort"
	"strconv"
	"strings"
)

func main() {
	reader := bufio.NewReader(os.Stdin)
	writer := bufio.NewWriter(os.Stdout)
	defer func(writer *bufio.Writer) {
		err := writer.Flush()
		if err != nil {
			panic(err)
		}
	}(writer)

	line, _ := reader.ReadString('\n')
	parts := strings.Fields(line)
	N, _ := strconv.Atoi(parts[0])
	M, _ := strconv.Atoi(parts[1])

	line, _ = reader.ReadString('\n')
	parts = strings.Fields(line)
	y1, _ := strconv.Atoi(parts[0])
	y2, _ := strconv.Atoi(parts[1])

	line, _ = reader.ReadString('\n')
	parts = strings.Fields(line)
	P := make([]int, N)
	for i := 0; i < N; i++ {
		P[i], _ = strconv.Atoi(parts[i])
	}

	line, _ = reader.ReadString('\n')
	parts = strings.Fields(line)
	Q := make([]int, M)
	for i := 0; i < M; i++ {
		Q[i], _ = strconv.Atoi(parts[i])
	}

	// 정렬
	sort.Ints(P)
	sort.Ints(Q)

	l, r := 0, 0
	maxGap := int(1e9)
	cnt := 0

	for l < N && r < M {

		temp := AbsInt(P[l] - Q[r])

		if temp < maxGap {
			maxGap = temp
			cnt = 1
		} else if temp == maxGap {
			cnt++
		}

		if P[l] > Q[r] {
			r++
		} else {
			l++
		}
	}
	fmt.Printf("%d %d", AbsInt(y1-y2)+maxGap, cnt)

}

func AbsInt(x int) int {
	if x < 0 {
		return -x
	}
	return x
}
