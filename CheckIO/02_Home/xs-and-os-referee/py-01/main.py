
def xo_referee(ls):
    a, b, c = ls[0], ls[1], ls[2]

    if (a+b+c).find(".") == -1:
        return "D"

    for e in (a, b, c):
        if len(set(list(e))) == 1:
            return e[0]

    return b[1]

if __name__ == '__main__':
    ex1 = xo_referee(["X.O", "XX.", "XOO"])  # "X", "Xs wins"
    print(ex1)
    ex2 = xo_referee(["OO.", "XOX", "XOX"])  # "O", "Os wins"
    print(ex2)
    ex3 = xo_referee(["OOX", "XXO", "OXX"])  # "D", "Draw"
    print(ex3)
    ex4 = xo_referee(["O.X", "XX.", "XOO"])  # "X", "Xs wins again"
    print(ex4)
    ex5 = xo_referee(["O.O ", "OO.", "XXX"]) # "X", "hp check"
    print(ex5)

