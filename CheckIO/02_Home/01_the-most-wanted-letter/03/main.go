package main

import (
	"fmt"
	"regexp"
	"sort"
	"strings"
)

func sorter(s string) string {
	low := strings.ToLower(s)
	ss := regexp.MustCompile(`[a-z]`).FindAllString(low, -1)
	sort.Strings(ss)

	var rslt string
	for _, v := range ss {
		rslt += string(v)
	}
	return rslt
}

func checker(s string) string {
	r := string(s[0])
	n := 1
	for _, v := range s {
		ea := strings.LastIndex(s, string(v)) - strings.Index(s, string(v))
		if ea > n {
			r = string(v)
			n = ea
		}
	}
	return r
}

func mostWanted(s string) string {
	str := sorter(s)
	rslt := checker(str)
	return rslt
}

func main() {
	var m1, m2, m3, m4, m5 string
	m1 = "Hello World!"
	m2 = "How do you do?"
	m3 = "One"
	m4 = "Oops!"
	m5 = "AAaooo!!!!"

	fmt.Println(mostWanted(m1)) //"l", "1st example"
	fmt.Println(mostWanted(m2)) //"o", "2nd example"
	fmt.Println(mostWanted(m3)) //"e", "3rd example"
	fmt.Println(mostWanted(m4)) //"o", "4th example"
	fmt.Println(mostWanted(m5)) //"a", "Letters"
}
