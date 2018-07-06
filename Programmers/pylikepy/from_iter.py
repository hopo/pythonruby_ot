
my_list = [[1, 2], [3, 4], [5, 6]]

# 00
answer = []
for i in my_list:
    answer += i


# 01
# 방법 1 - sum 함수
answer = sum(my_list, [])

# 방법 2 - itertools
import itertools
list(itertools.chain.from_iterable(my_list))
