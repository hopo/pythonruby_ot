# ...ing

def safe_pawns(pawns):
    ls = list()
    for e in pawns:
        ls.append(int(e[1]))
    
    cnt = 0
    mn = min(ls)
    for e in ls:
        if e != mn:
            cnt += 1

    return cnt

if __name__ == '__main__':
    ex1 = safe_pawns({"b4", "d4", "f4", "c3", "e3", "g5", "d2"}) # 6 , safe 6
    print(ex1)
    ex2 = safe_pawns({"b4", "c4", "d4", "e4", "f4", "g4", "e5"}) # 1
    print(ex2)
    ex3 = safe_pawns(["a1","a2","a3","a4","h1","h2","h3","h4"]) # 0
    print(ex3)
