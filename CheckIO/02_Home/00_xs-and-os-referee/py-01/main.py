# ...ing

def xo_referee(game_result):
    return "D"

if __name__ == '__main__':
    ex1 = xo_referee(["X.O", "XX.", "XOO"])  # "X", "Xs wins"
    print(ex1)
    ex2 = xo_referee(["OO.", "XOX", "XOX"])  # "O", "Os wins"
    print(ex2)
    ex3 = xo_referee(["OOX", "XXO", "OXX"])  # "D", "Draw"
    print(ex3)
    ex4 = xo_referee(["O.X", "XX.", "XOO"])  # "X", "Xs wins again"
    print(ex4)
    ex5 = xo_referee(["O.O ", "OO.", "XXX"]) # "X"
    print(ex5)
    ex6 = xo_referee(["OXO","XOX","OXO"]) # "O"
    print(ex6)

