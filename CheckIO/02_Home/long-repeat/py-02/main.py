
def long_repeat(line):
    if line == '':
        return 0

    cnt = 0
    chk = line[0]
    ls = list()

    for e in line:
        if chk == e:
            cnt += 1
        else:
            ls.append(cnt)
            cnt = 1
            chk = e

    ls.append(cnt)

    return max(ls)


if __name__ == '__main__':
    ex1 = long_repeat('sdsffffse')  # 4, "First"
    print(ex1)
    ex2 = long_repeat('ddvvrwwwrggg')  # 3, "Second"
    print(ex2)
    ex3 = long_repeat('')  # 0
    print(ex3)
    ex4 = long_repeat('aa')  # 2
    print(ex4)
