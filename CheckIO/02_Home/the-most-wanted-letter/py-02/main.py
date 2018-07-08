
def most_wanted(data):
    alpls = []
    for e in data:
        if ord(e) >= ord('A') and ord(e) <= ord('z'):
            alpls.append(e.lower())

    alpls.sort()

    most = alpls[0]
    mx = 1
    cnt = 1

    for i in range(1, len(alpls)):
        if alpls[i] != alpls[i-1]:
            if mx < cnt:
                most = alpls[i-1]
                mx = cnt
            cnt = 1
        else:
            cnt += 1

    if mx < cnt:
        most = alpls[len(alpls)-1]

    return most


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
