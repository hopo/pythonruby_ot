
def find_message(text):
    ret = str()
    for v in text:
        if v.isupper():
            ret += v

    return ret

if __name__ == '__main__':
    ex1 = find_message("How are you? Eh, ok. Low or Lower? Ohhh.") # "HELLO"
    print(ex1)

    ex2 = find_message("hello world!") # "", "Nothing"
    print(ex2)

    ex3 = find_message("HELLO WORLD!!!") # "HELLOWORLD", "Capitals"
    print(ex3)

