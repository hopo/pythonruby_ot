def solution(no, works):
	lnth = len(works)
	total = sum(works) - no

	each = total // lnth
	remainder = total % lnth

	result = 0
	for i in range(remainder, lnth):
		result += pow(each, 2)

	for i in range(remainder):
		result += pow(each + 1, 2)

	return result


res1 = solution(4, [4,3,3]) #12
print(res1)

# res2 = solution(2, [3,3,3]) #17
# print(res2)