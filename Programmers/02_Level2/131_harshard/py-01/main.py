
def Harshad(n):
    il = list()
    for s in str(n):
        il.append(int(s))
    return n%sum(il) == 0

if __name__ == '__main__':
    print(Harshad(18)) # True, 18/(1+8) % = 0
    print(Harshad(12)) # True, 12/(1+2) % = 0
    print(Harshad(11)) # False, 11/(1+1) % = 1
    print(Harshad(13)) # False, 13/(1+3) % = 1
