# quiz3-CandidateKey.py
# ing

def solution(relation):
	cols = len(relation[0])

	dct = dict()
	lst = list()

	for c in range(cols): 
		for reco in relation:
			lst.append(reco[c])
		key = 'col{}'.format(c)
		dct[key] = lst
		lst = []

	for d in dct:
		if len(dct[d]) == len(set(dct[d])):
			print("!!!!!")

	return ''

relation = [
    ["100", "ryan", "music", "2"],
    ["200", "apeach", "math", "2"],
    ["300", "tube", "computer", "3"],
    ["400", "con", "computer", "4"],
    ["500", "muzi", "music", "3"],
    ["600", "apeach", "music", "2"]
]
result = 2

if __name__ == '__main__':
	ex = solution(relation)
	print(ex)
