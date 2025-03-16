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
			panic("Failed to flush bufio writer")
		}
	}(writer)

	N := readInt(reader)

	nums := readIntArray(reader, N)

	sortedNums := make([]int, N)
	copy(sortedNums, nums)
	sort.Ints(sortedNums)

	pos := make(map[int]int, N)
	for i, v := range sortedNums {
		pos[v] = i
	}

	visited := make([]bool, N)
	ans := 0

	for i := 0; i < N; i++ {
		if !visited[i] {
			ans += solve(i, visited, nums, pos)
		}
	}

	_, _ = fmt.Fprintln(writer, ans)
}

func solve(idx int, visited []bool, nums []int, pos map[int]int) int {
	rst := 0
	curIdx := idx

	for !visited[curIdx] {
		visited[curIdx] = true
		curVal := nums[curIdx]
		nextPos := pos[curVal]

		if nextPos == curIdx || visited[nextPos] {
			break
		}

		rst++
		curIdx = nextPos
	}

	return rst
}

func readInt(reader *bufio.Reader) int {
	line, _ := reader.ReadString('\n')
	n, _ := strconv.Atoi(strings.TrimSpace(line))
	return n
}

func readIntArray(reader *bufio.Reader, size int) []int {
	line, _ := reader.ReadString('\n')
	fields := strings.Fields(line)

	arr := make([]int, size)
	for i := 0; i < size; i++ {
		arr[i], _ = strconv.Atoi(fields[i])
	}
	return arr
}
