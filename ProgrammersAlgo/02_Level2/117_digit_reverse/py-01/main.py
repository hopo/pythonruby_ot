
def digit_reverse(n):
    l = list()
    for s in str(n):
        l.insert(0, int(s)) 
    return l

if __name__ == '__main__':
    ex1 = digit_reverse(12345) # [5, 4, 3, 2, 1]
    print(ex1)

