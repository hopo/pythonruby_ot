# quiz4-Meokbang.py
# ing

def solution(food_times, k):
	sec = 0
	lnth = len(food_times)

	while sec != k:
		if food_times[sec % lnth] == 0:
			if ((sec % lnth) + 1) == lnth:
				food_times[0] -= 1
			else:
				food_times[(sec % lnth) + 1] -= 1
		else:
			food_times[sec % lnth] -= 1
		print(food_times)
		sec += 1

	return -1


food_times1 = [3, 1, 2]
k1 = 5
ex1 = solution(food_times1, k1) #1
print(ex1)
