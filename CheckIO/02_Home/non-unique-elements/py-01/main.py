# https://py.checkio.org/mission/non-unique-elements/solve/

def checkio(data):
    for e in set(data):
        idx = data.index(e)
        try:
            data.index(e, idx+1)
        except:
            data.remove(e)

    return data

if __name__ == "__main__":
    ex1 = checkio([1, 2, 3, 1, 3]) # [1, 3, 1, 3], "1st example"
    print(ex1)
    ex2 = checkio([1, 2, 3, 4, 5]) # [], "2nd example"
    print(ex2)
    ex3 = checkio([5, 5, 5, 5, 5]) # [5, 5, 5, 5, 5], "3rd example"
    print(ex3)
    ex4 = checkio([10, 9, 10, 10, 9, 8]) # [10, 9, 10, 10, 9], "4th example"
    print(ex4)

