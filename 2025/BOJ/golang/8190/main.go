package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

const MAX_K = 31
const INF int64 = 1e18

func kmp(a, b string) int64 {
	s := b + "#" + a
	lps := make([]int, len(s))
	for i := 1; i < len(s); i++ {
		j := lps[i-1]
		for j > 0 && s[i] != s[j] {
			j = lps[j-1]
		}
		if s[i] == s[j] {
			j++
		}
		lps[i] = j
	}
	return int64(lps[len(s)-1])
}

func min(a, b int64) int64 {
	if a < b {
		return a
	}
	return b
}

func main() {
	reader := bufio.NewReader(os.Stdin)
	scanner := bufio.NewScanner(reader)
	scanner.Split(bufio.ScanLines)

	scanner.Scan()
	parts := strings.Fields(scanner.Text())
	n, _ := strconv.Atoi(parts[0])
	m, _ := strconv.Atoi(parts[1])
	m -= 1

	names := make([]string, n)
	lengths := make([]int64, n)

	for i := 0; i < n; i++ {
		scanner.Scan()
		names[i] = strings.TrimSpace(scanner.Text())
		lengths[i] = int64(len(names[i]))
	}

	f := make([][][]int64, MAX_K)
	for k := 0; k < MAX_K; k++ {
		f[k] = make([][]int64, n)
		for i := 0; i < n; i++ {
			f[k][i] = make([]int64, n)
			for j := 0; j < n; j++ {
				f[k][i][j] = INF
			}
		}
	}

	for i := 0; i < n; i++ {
		for j := 0; j < n; j++ {
			var o int64
			if i == j {
				if lengths[j] > 1 {
					o = kmp(names[i], names[j][:lengths[j]-1])
				}
			} else {
				o = kmp(names[i], names[j])
			}
			f[0][i][j] = lengths[j] - o
		}
	}

	for k := 1; k < MAX_K; k++ {
		for i := 0; i < n; i++ {
			for j := 0; j < n; j++ {
				for t := 0; t < n; t++ {
					f[k][i][j] = min(f[k][i][j], f[k-1][i][t]+f[k-1][t][j])
				}
			}
		}
	}

	dis := make([]int64, n)
	copy(dis, lengths)

	for k := 0; k < MAX_K; k++ {
		if (m>>uint(k))&1 == 1 {
			tmp := make([]int64, n)
			for i := range tmp {
				tmp[i] = INF
			}
			for i := 0; i < n; i++ {
				for j := 0; j < n; j++ {
					tmp[j] = min(tmp[j], dis[i]+f[k][i][j])
				}
			}
			dis = tmp
		}
	}

	ans := INF
	for i := 0; i < n; i++ {
		ans = min(ans, dis[i])
	}
	fmt.Println(ans)
}
