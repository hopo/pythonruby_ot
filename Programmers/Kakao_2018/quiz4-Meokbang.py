# quiz4-Meokbang.py
# ing

def solution(food_times, k):
	lnth = len(food_times)

	cha = sum(food_times) - k

	ftimes = sorted(food_times, reverse=True)
	x = food_times.index(ftimes[cha-1])

	return x+1


food_times = [3, 1, 2]
k = 5
ex = solution(food_times, k) #1
print(ex)
