def solution(no, works):
	total = sum(works) - no

	each = total // len(works)
	remainder = total % len(works)

	result = 0
	for i in works:
		if remainder > 0:
			result += pow(each + 1, 2)
			remainder -= 1
		else:
			result += pow(each, 2)

	return result


res1 = solution(4, [4,3,3]) #12
print(res1)

res2 = solution(2, [3,3,3]) #17
print(res2)