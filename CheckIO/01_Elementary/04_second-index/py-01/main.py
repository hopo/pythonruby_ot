
# ...ing
"""
func second_index(text string, symbol string) int {
	tsl := []byte(text)
	sym := []byte(symbol)
	var box []int
	for i, v := range tsl {
		if v == sym[0] {
			box = append(box, i)
		}
	}
	if len(box) < 2 {
		return -1
	}
	return box[1]
}
"""
def second_index(text, symbol):
    n = text.index(symbol)
    return n
    

if __name__ == '__main__':
    ex1 = second_index("sims", "s") # 3, "First"
    print(ex1)
    ex2 = second_index("find the river", "e") # 12, "Second"
    print(ex2)
    ex3 = second_index("hi", " ") # -1, "Third"
    print(ex3)
    ex4 = second_index("hi mayor", " ") # -1, "Fourth"
    print(ex4)
    ex5 = second_index("hi mr Mayor", " ") # 5, "Fifth"
    print(ex5)
    
    
