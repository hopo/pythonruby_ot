def solution(arr):
	num = 0
	arr.sort()
	for a in arr:
		num += 1
		if a != num:
			return False

	return len(arr) == arr[len(arr)-1]


testArr1 = [4, 1, 3, 2]
result1 = solution(testArr1)
print(result1)

# testArr2 = [4,1,3]
# result2 = solution(testArr2)
# print(result2)
