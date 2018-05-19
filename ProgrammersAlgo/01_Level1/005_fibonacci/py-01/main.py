
def fibonacci(num): # (int) list
    a, b = 1, 0
    while num != 0:
        a, b = a+b, a
        num -= 1
    return b

# 아래는 테스트로 출력해 보기 위한 코드입니다.
if __name__ == '__main__':
    print(fibonacci(3)) # 2, [1, 1, 2]
    print(fibonacci(4)) # 3, [1, 1, 2, 3]
    print(fibonacci(6)) # 8, [1, 1, 2, 3, 5, 8]
