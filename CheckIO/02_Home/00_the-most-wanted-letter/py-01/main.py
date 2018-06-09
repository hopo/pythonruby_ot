
def most_wanted(data):
    ls = list(data.lower())
    ls.sort()

    box = []
    for e in ls:
        if e.isalpha():
            box.append(e)

    mx = 1
    cnt = 1
    most = box[0]
    target = box[0]

    for i in range(1, len(box)):
        if target != box[i]:
            if mx < cnt:
                mx = cnt
                most = box[i-1]
            cnt = 1
            target = box[i]
        else:
            cnt += 1

    return most

if __name__ == '__main__':
    ex1 = most_wanted("Hello World!") # "l", "1st example"
    print(ex1)
    ex2 = most_wanted("How do you do?")   # "o", "2nd example"
    print(ex2)
    ex3 = most_wanted("One")  # "e", "3rd example"
    print(ex3)
    ex4 = most_wanted("Oops!")    # "o", "4th example"
    print(ex4)
    ex5 = most_wanted("AAaooo!!!!")   # "a", "Letters"
    print(ex5)
