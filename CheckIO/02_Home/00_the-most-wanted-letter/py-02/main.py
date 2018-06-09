# ...ing

def most_wanted(text):
    box = list(text.lower())
    box.sort()

    mx = 1
    cnt = 1
    most = box[0]
    target = box[0]

    for i in range(1, len(box)):
        if ord(box[i]) >= ord('A') and ord(box[i]) <= ord('z'):
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
    '''
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
    '''
    ex6 = most_wanted("Aaaaaaaaaaaaaaaa!!!!") # "a"
    print(ex6)

