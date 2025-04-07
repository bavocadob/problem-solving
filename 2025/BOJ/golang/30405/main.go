package main

import (
	"bufio"
	"os"
	"sort"
	"strconv"
)

var sc = bufio.NewScanner(os.Stdin)
var bw = bufio.NewWriter(os.Stdout)

func main() {
	defer bw.Flush()
	sc.Split(bufio.ScanWords)

	N, _ := nextInt(), nextInt()
	gates := make([]int, N*2)

	for i := 0; i < N; i++ {
		k := nextInt()

		for j := 0; j < k; j++ {
			temp := nextInt()
			if j == 0 {
				gates[i*2] = temp
			} else if j == (k - 1) {
				gates[i*2+1] = temp
			}
		}
	}

	sort.Ints(gates)
	bw.WriteString(strconv.Itoa(gates[N-1]))

}

func nextInt() int {
	sc.Scan()
	i, _ := strconv.Atoi(sc.Text())
	return i
}
