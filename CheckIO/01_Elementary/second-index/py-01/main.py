
def second_index(text, symbol):
    cnt = idx = 0
    for i in range(len(text)):
        if text[i] == symbol:
            idx = i
            cnt += 1
    return cnt == 2 and idx or None
    

if __name__ == '__main__':
    ex1 = second_index("sims", "s") # 3, "First"
    print(ex1)
    ex2 = second_index("find the river", "e") # 12, "Second"
    print(ex2)
    ex3 = second_index("hi", " ") # None, "Third"
    print(ex3)
    ex4 = second_index("hi mayor", " ") # None, "Fourth"
    print(ex4)
    ex5 = second_index("hi mr Mayor", " ") # 5, "Fifth"
    print(ex5)
    
