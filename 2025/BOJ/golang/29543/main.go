package main

import (
	"bufio"
	"fmt"
	"os"
)

func main() {
	reader := bufio.NewReader(os.Stdin)
	writer := bufio.NewWriter(os.Stdout)
	defer func(writer *bufio.Writer) {
		err := writer.Flush()
		if err != nil {

		}
	}(writer)

	var N int
	_, _ = fmt.Fscan(reader, &N)

	switch N {
	case 1:
		fmt.Fprint(writer, "9")
	case 2:
		fmt.Fprint(writer, "99")
	case 3:
		fmt.Fprint(writer, "989")
	case 4:
		fmt.Fprint(writer, "9889")
	case 5:
		fmt.Fprint(writer, "97679")
	case 6:
		fmt.Fprint(writer, "976679")
	case 7:
		fmt.Fprint(writer, "9643469")
	case 8:
		fmt.Fprint(writer, "96433469")
	default:
		fmt.Fprint(writer, "-1")
	}
}
