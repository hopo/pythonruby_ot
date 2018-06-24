# ...ing


def most_wanted(data):
    ls = list(data.lower())
    ls.sort()
    for e in ls:
        b = e.isalpha()
        print(b)


    return ''


if __name__ == '__main__':
    ex1 = most_wanted("Hello World!")  # "l", "1st example"
    print(ex1)
    '''
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
    '''
