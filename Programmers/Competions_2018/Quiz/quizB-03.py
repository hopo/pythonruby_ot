# I can not Jechool this solution

def solution(no, works):
	works.sort()

	for n in range(no):
		works[len(works)-1-n] -= 1

	for i in range(len(works)):
		works[i] = pow(works[i], 2)

	return sum(works)


res1 = solution(4, [4,3,3]) #12
print(res1)

res2 = solution(2, [3,3,3]) #17
print(res2)