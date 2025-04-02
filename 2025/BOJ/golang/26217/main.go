package main

import (
	"bufio"
	"os"
	"strconv"
)

var sc = bufio.NewScanner(os.Stdin)
var bw = bufio.NewWriter(os.Stdout)

func main() {
	defer bw.Flush()
	sc.Split(bufio.ScanWords)

	n := nextInt()

	ans := 0.0

	for i := 0; i < n; i++ {
		ans += float64(n) / float64(n-i)
	}
	bw.WriteString(strconv.FormatFloat(ans, 'f', -1, 64))

}

func nextInt() int {
	sc.Scan()
	i, _ := strconv.Atoi(sc.Text())
	return i
}
