# quiz2-Stage.py
# ing

import collections

def solution(N, stages):
  arr = sorted(stages)
  lnth = len(stages)
  cols = collections.Counter(stages)

  bunmo = lnth
  aft = dict()
  ser = list()

  for i in range(1, N+1):
    aft[i] = cols[i] / bunmo
    ser.append(cols[i] / bunmo)

    bunmo = bunmo-cols[i]

  sortser = sorted(ser, reverse=True)

  retarr = list()

  for i in sortser:
    finded = ser.index(i)
    if (finded + 1 in retarr):
      finded = ser.index(i, finded+1)

    retarr.append(finded + 1)

  return retarr




N1 = 5
stages1 = [2, 1, 2, 6, 2, 4, 3, 3] # [3, 4, 2, 1, 5]
N2 = 4
stages2 = [4, 4, 4, 4, 4] # [4, 1, 2, 3]

if __name__ == '__main__':
  ex1 = solution(N1, stages1)
  print(ex1)

  ex2 = solution(N2, stages2)
  print(ex2)


