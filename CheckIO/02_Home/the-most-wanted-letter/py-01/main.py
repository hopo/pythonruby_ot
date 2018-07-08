
def most_wanted(data):
    ls = list(data.lower())
    ls.sort()

    alpls = []
    for e in ls:
        if ord(e) >= 97 and ord(e) <= 122:
            alpls.append(e)

    dc = {}
    cnt = 1
    dc[alpls[0]] = cnt

    for i in range(1, len(alpls)):
        if alpls[i] != alpls[i-1]:
            cnt = 0
        cnt = cnt + 1
        dc[alpls[i]] = cnt

    mx = max(list(dict.values(dc)))

    for e in dc:
        if dc[e] == mx:
            return e

    return ''


if __name__ == '__main__':
    ex1 = most_wanted("Hello World!")  # "l", "1st example"
    print(ex1)
    ex2 = most_wanted("How do you do?")   # "o", "2nd example"
    print(ex2)
    ex3 = most_wanted("One")  # "e", "3rd example"
    print(ex3)
    ex4 = most_wanted("Oops!")    # "o", "4th example"
    print(ex4)
    ex5 = most_wanted("AAaooo!!!!")   # "a", "Letters"
    print(ex5)
    ex6 = most_wanted("Aaaaaaaaaaaaaaaa!!!!")  # "a"
    print(ex6)
    ex7 = most_wanted("abb")  # "b"
    print(ex7)
    ex8 = most_wanted("a-b")  # "a"
    print(ex8)
