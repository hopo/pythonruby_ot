# https://docs.python.org/3/library/functions.html#int

num = '3212'
base = 5

# case A
answer = 0
for idx, i in enumerate(num[::-1]):
    answer += int(i) * ( base ** idx )
print(answer)

# case B
print(int(num, base))

