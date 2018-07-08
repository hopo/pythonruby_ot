
def checkio(data):
    if len(data) < 10:
        return False

    bupp = blow = bdig = False

    for d in data:
        if not bupp and d.isupper():
            bupp = True
        if not blow and d.islower():
            blow = True
        if not bdig and d.isdigit():
            bdig = True

    return bupp and blow and bdig


if __name__ == '__main__':
    ex1 = checkio('A1213pokl')  # False, "1st example"
    print(ex1)
    ex2 = checkio('bAse730onE4')  # True, "2nd example"
    print(ex2)
    ex3 = checkio('asasasasasasasaas')  # False, "3rd example"
    print(ex3)
    ex4 = checkio('QWERTYqwerty')  # False, "4th example"
    print(ex4)
    ex5 = checkio('123456123456')  # False, "5th example"
    print(ex5)
    ex6 = checkio('QwErTy911poqqqq')  # True, "6th example"
    print(ex6)
