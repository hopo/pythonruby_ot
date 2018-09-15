def solution(arr):
	sarr = sorted(arr)
	i = 1
 	for e in sarr:
		if e != i:
			return False 
		i += 1
	return True


arr1 = [4, 1, 3, 2]	#true
arr2 = [4, 1, 3]	#false

result1 = solution(arr1)
print(result1)

result2 = solution(arr2)
print(result2)