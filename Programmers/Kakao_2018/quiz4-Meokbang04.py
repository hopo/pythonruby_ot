# quiz4-Meokbang.py
# ing

def solution(food_times, k):
	idx = 0
	op = 0
	lnth = len(food_times)

	while k != 0:
		idx = op%lnth

		if food_times[idx] == 0:
			op += 1
			continue
		else:
			food_times[idx] -= 1

		k -= 1
		op += 1

	return op%lnth + 1


food_times = [3, 1, 2]
k = 5
ex = solution(food_times, k) #1
print(ex)
