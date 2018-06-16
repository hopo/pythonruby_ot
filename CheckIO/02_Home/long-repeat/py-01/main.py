
def long_repeat(line):
    if line == '':
        return 0

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

    return mx == 0 and cnt or mx

if __name__ == '__main__':
    ex1 = long_repeat('sdsffffse') # 4, "First"
    print(ex1)
    ex2 = long_repeat('ddvvrwwwrggg') # 3, "Second"
    print(ex2)
    ex3 = long_repeat('') # 0
    print(ex3)
    ex4 = long_repeat('aa') # 2
    print(ex4)

