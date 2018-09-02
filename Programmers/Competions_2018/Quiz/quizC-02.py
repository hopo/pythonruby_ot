def solution(n, signs):
	des = []

	for s in signs:
		for i in range(len(s)):
			if s[i] == 1:
				des.append(i)
				
	result = [[0 for x in range(n)] for y in range(n)] 

	for i in range(n):
		for d in des:
			result[i][d] = 1
	return result


res1 = solution(3, [[0,1,0],[0,0,1],[1,0,0]]) #[[1,1,1],[1,1,1],[1,1,1]]
print(res1)

res2 = solution(3, [[0,0,1],[0,0,1],[0,1,0]]) #[[0,1,1],[0,1,1],[0,1,1]]
print(res2)

