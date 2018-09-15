# quiz4-Meokbang.py
# ing

def solution(food_times, k):
	sec = 0
	idx = 0
	i = 0
	lnth = len(food_times)

	while sec != k:
		idx = i % lnth

		if food_times[idx] == 0:
			idx += 1
			
		food_times[idx] -= 1

		sec += 1
		i += 1

		print('sec: {}, idx: {}, result: {} '.format(sec, idx, food_times))

	return ''


food_times = [3, 1, 2]
k = 5
ex = solution(food_times, k) #1
print(ex)
