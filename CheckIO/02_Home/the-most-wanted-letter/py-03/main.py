# Others


def most_wanted(text):
    numbers = [text.lower().count(chr(c + 97)) for c in range(26)]
    return chr(numbers.index(max(numbers)) + 97)


if __name__ == '__main__':
    ex1 = most_wanted("Hello World!")  # "l", "1st example"
    print(ex1 == 'l')
    ex2 = most_wanted("How do you do?")   # "o", "2nd example"
    print(ex2 == 'o')
    ex3 = most_wanted("One")  # "e", "3rd example"
    print(ex3 == 'e')
    ex4 = most_wanted("Oops!")    # "o", "4th example"
    print(ex4 == 'o')
    ex5 = most_wanted("AAaooo!!!!")   # "a", "Letters"
    print(ex5 == 'a')
    ex6 = most_wanted("Aaaaaaaaaaaaaaaa!!!!")  # "a"
    print(ex6 == 'a')
    ex7 = most_wanted("abb")  # "b"
    print(ex7 == 'b')
    ex8 = most_wanted("a-b")  # "a"
    print(ex8 == 'a')
