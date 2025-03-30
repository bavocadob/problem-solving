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

	var coins []int

	n, k := nextInt(), nextInt()

	for i := 1; i <= n; i++ {
		temp := 0
		cur := i

		for cur > 0 {
			temp += cur % 10
			cur /= 10
		}

		if i%temp == 0 {
			coins = append(coins, i)
		}
	}

	dp := make([]int, n+1)
	dp[0] = 1
	for _, coin := range coins {

		for i := coin; i <= n; i++ {
			dp[i] = (dp[i] + dp[i-coin]) % k
		}

	}

	_, _ = bw.WriteString(strconv.Itoa(dp[n]))

}

func nextInt() int {
	sc.Scan()
	i, _ := strconv.Atoi(sc.Text())
	return i
}
