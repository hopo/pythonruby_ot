def solution(n, m):
	count = 0
	for num in range(n, m):
		if is_palin(num):
			count += 1 
	return count

def is_palin(num):
	st = str(num)
	for i in range(len(st)//2):
		if st[i] != st[len(st)-1-i]:
			return False
	return True

res1 = solution(1, 100) #18
print(res1)

res2 = solution(100, 300) #20
print(res2)