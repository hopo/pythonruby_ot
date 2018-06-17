
from typing import List, Any

def all_the_same(elements: List[Any]) -> bool:
    ret = True
    lnth = len(set(elements))
    if lnth > 1:
        ret = False
    return ret


if __name__ == '__main__':
    ex1 = all_the_same([1, 1, 1]) # True
    print(ex1)
    ex2 = all_the_same([1, 2, 1]) # False
    print(ex2)
    ex3 = all_the_same(['a', 'a', 'a']) # True
    print(ex3)
    ex4 = all_the_same([]) # True
    print(ex4)
    ex5 = all_the_same([1]) # True
    print(ex5)

