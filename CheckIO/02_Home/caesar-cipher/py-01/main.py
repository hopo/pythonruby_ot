
def to_encrypt(text, delta):
    ret = list()
    for e in text:
        if e == ' ':
            ret.append(' ')
        else:
            b = ord(e) + delta
            if b < 97:
                b += 26
            if b > 122:
                b -= 26
            ret.append(chr(b))
    return str().join(ret)


if __name__ == '__main__':
    ex1 = to_encrypt("a b c", 3)  # "d e f"
    print(ex1)
    ex2 = to_encrypt("a b c", -3)  # "x y z"
    print(ex2)
    ex3 = to_encrypt("simple text", 16)  # "iycfbu junj"
    print(ex3)
    ex4 = to_encrypt("important text", 10)  # "swzybdkxd dohd"
    print(ex4)
    ex5 = to_encrypt("state secret", -13)  # "fgngr frperg"
    print(ex5)
