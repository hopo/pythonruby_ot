# https://docs.python.org/3/library/stdtypes.html?highlight=rjust#str.ljust

s = 'abc'
n = 7

# caseA
answer = ''
for i in range(n-len('가나다라')):
    answer += ' '
answer += '가나다라'
print(answer)


# caseB
s = 'abc'
n = 7

print(s.ljust(n))
print(s.rjust(n))
print(s.center(n))
