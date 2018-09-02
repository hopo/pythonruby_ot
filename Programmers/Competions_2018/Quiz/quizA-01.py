def solution(n, m):
	x = len(str(m))
	pea = palin(x)
	
	return pea

def palin(num):
	if num == 2:
		return 9
	return 9 * (palin(num-1) + pow(10, num - 3))


# res1 = solution(1, 100) #18
# print(res1)

res2 = solution(100, 300) #20
print(res2)