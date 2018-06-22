package main

import (
	"fmt"
)

func main() {
	ex1 := bestSet(3, 13) // [4 4 5]
	ex2 := bestSet(4, 14) // [3 3 4 4]
	fmt.Println(ex1)
	fmt.Println(ex2)
}

func bestSet(n, s int) []int {
	// proof 4*4*5 is most big number
	var ret []int
	de := s / n
	r := s % n
	x := 1
	for i := 0; i < n; i++ {
		x = 0
		if r != 0 {
			x = 1
			r--
		}
		ret = append([]int{de + x}, ret...)
	}

	return ret
}
