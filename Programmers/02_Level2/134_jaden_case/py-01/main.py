
def Jaden_Case(s):
    ret = ''
    flag = True
    cli = s.lower()

    for x in cli:
        if x == ' ':
            flag = True
        elif flag:
            flag = False
            x = x.upper()
        ret += x
        
    return ret

if __name__ == '__main__':
    ex1 = Jaden_Case("3people unFollowed me for the last week") # 3people Unfollowed Me For The Last Week
    print(ex1)

    ex2 = Jaden_Case("Press ENTER or type command to continue") # Press Enter Or Type Command To Continue
    print(ex2)
