
def easy_unpack(elements):
    return (elements[0], elements[2], elements[-2])

if __name__ == '__main__':
    ex1 = easy_unpack((1, 2, 3, 4, 5, 6, 7, 9)) # (1, 3, 7)
    print(ex1)
    ex2 = easy_unpack((1, 1, 1, 1)) # (1, 1, 1)
    print(ex2)
    ex3 = easy_unpack((6, 3, 7)) # (6, 7, 3)
    print(ex3)
