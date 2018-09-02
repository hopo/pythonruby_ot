def solution(arr):
	num = 0
	lnth = 0

	for l in arr: lnth += 1

	for i in range(lnth - 1):
		for j in range(i, lnth):
			if arr[i] > arr[j]:
				arr[i], arr[j] = arr[j], arr[i]

	for a in arr:
		num += 1
		if a != num:
			return False

	return lnth == arr[lnth-1]


testArr1 = [4, 1, 3, 2]
result1 = solution(testArr1)
print(result1)

testArr2 = [4,1,3]
result2 = solution(testArr2)
print(result2)
