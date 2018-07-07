# 00

# 재귀함수를 이용해 만든 permutation 함수


def permutation(iterable, n, r):
    if r == 0:
        print(iterable)
        return
    for i in range(n-1, -1, -1):
        iterable[i], iterable[i-1] = iterable[i-1], iterable[i]
        permutation(iterable, n-1, r-1)
        iterable[i], iterable[i-1] = iterable[i-1], iterable[i]


pool = ['A', 'B', 'C']
permutation(pool, len(pool), len(pool))


# 01
# https://docs.python.org/3/library/itertools.html#itertools.permutations

import itertools

pool = ['A', 'B', 'C']
print(list(map(''.join, itertools.permutations(pool))))  # 3개의 원소로 수열 만들기
print(list(map(''.join, itertools.permutations(pool, 2))))  # 2개의 원소로 수열 만들기
