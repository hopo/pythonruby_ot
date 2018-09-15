# quiz2-Stage.py
# ing

import collections
import operator

def solution(N, stages):
  lnth = len(stages)
  cols = collections.Counter(stages)

  dct = dict()

  for i in range(1, N+1):
    dct[i] = cols[i] / lnth
    lnth = lnth-cols[i]

  ret = list()
  soso = sorted(dct.items(), key=operator.itemgetter(1), reverse=True)
  for k, y in soso:
    ret.append(k)

  return ret


N1 = 5
stages1 = [2, 1, 2, 6, 2, 4, 3, 3] # [3, 4, 2, 1, 5]
N2 = 4
stages2 = [4, 4, 4, 4, 4] # [4, 1, 2, 3]

if __name__ == '__main__':
  ex1 = solution(N1, stages1)
  print(ex1)

  # ex2 = solution(N2, stages2)
  # print(ex2)


