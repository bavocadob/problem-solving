package main

import (
	"bufio"
	"os"
	"sort"
	"strconv"
)

var br = bufio.NewReader(os.Stdin)
var sc = bufio.NewScanner(os.Stdin)
var bw = bufio.NewWriter(os.Stdout)

func main() {
	defer bw.Flush()
	sc.Split(bufio.ScanWords)

	n, k, t := nextInt(), nextInt(), nextInt()

	nums := make([]int, n)
	for i := 0; i < n; i++ {
		nums[i] = nextInt() % k
	}

	sort.Ints(nums)

	acc := 0

	for i := 0; i < t; i++ {
		q := nextInt()
		acc = (acc + q) % k

		target := k - acc - 1
		idx := lowerBound(nums, target)

		var ans int

		if idx == -1 {
			ans = (nums[n-1] + acc) % k
		} else {
			ans = (nums[idx] + acc) % k
		}
		bw.WriteString(strconv.Itoa(ans) + " ")

	}
	bw.WriteString("\n")

}

func lowerBound(nums []int, target int) int {
	left, right := 0, len(nums)-1
	rst := -1
	for left <= right {
		mid := (left + right) / 2
		if nums[mid] <= target {
			rst = mid
			left = mid + 1
		} else {
			right = mid - 1
		}
	}

	return rst
}

func nextInt() int {
	sc.Scan()
	i, _ := strconv.Atoi(sc.Text())
	return i
}
