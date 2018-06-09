package main

import (
	"fmt"
	"strconv"
)

func main() {
	fmt.Println(hammingDistance(117, 17)) //3, "First example"
	fmt.Println(hammingDistance(1, 2))    //2, "Second example"
	fmt.Println(hammingDistance(16, 15))  //5, "Third example"
	fmt.Println(hammingDistance(256, 8))  //2, "hp ex""
}

func hammingDistance(n, m int) (ret int) {
	if n == m {
		return 0
	}

	x := bConverter(n)
	y := bConverter(m)

	lx := len(x)
	ly := len(y)

	var l int

	if lx != ly {
		switch {
		case lx > ly:
			d := lx - ly
			y = zeroMulti(d) + y
			l = lx

		case lx < ly:
			d := ly - lx
			x = zeroMulti(d) + x
			l = ly
		}
	}

	for i := 0; i < l; i++ {
		if x[i] != y[i] {
			ret++
		}
	}

	return
}

func bConverter(num int) string {
	s := strconv.FormatInt(int64(num), 2)
	return s
}

func zeroMulti(d int) string {
	z := "0"

	var s string
	for i := 0; i < d; i++ {
		s += z
	}
	return s
}
