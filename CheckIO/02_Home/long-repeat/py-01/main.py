
def long_repeat(line):
    char = line[0]
    cnt = 0
    mx = 0
    for e in line:
        if char == e:
            cnt += 1
        else:
            if mx < cnt:
                mx = cnt
            char = e
            cnt = 1 
    return mx

if __name__ == '__main__':
    ex1 = long_repeat('sdsffffse') # 4, "First"
    print(ex1)
    ex2 = long_repeat('ddvvrwwwrggg') # 3, "Second"
    print(ex2)

