
def first_word(text: str) -> str:
    ret = ''
    begin = False
    for s in text:
        if not begin:
            if s.isalpha(): begin = True
            else: continue
        if s == ' ' or s == '.' or s == ',':
            break
        ret += s
    return ret

if __name__ == '__main__':
    ex1 = first_word("Hello world") # "Hello"
    print(ex1)
    ex2 = first_word(" a word ") # "a"
    print(ex2)
    ex3 = first_word("don't touch it") # "don't"
    print(ex3)
    ex4 = first_word("greetings, friends") # "greetings"
    print(ex4)
    ex5 = first_word("... and so on ...") # "and"
    print(ex5)
    ex6 = first_word("hi") # "hi"
    print(ex6)
    ex7 = first_word("Hello.World") # "Hello"
    print(ex7)

