# quiz1-Chating.py

def solution(record):
  answer = list()
  dctId = dict()

  for rec in record:
    spl = rec.split(' ')
    answer.append((spl[1], spl[0]))

    if len(spl) == 3:
      dctId[spl[1]] = spl[2]

  tran = ''
  ret = list()
  for user, msg in answer:
    if msg == 'Enter':
      tran = '들어왔습니다.'
    elif msg == 'Leave':
      tran = '나갔습니다.'
    elif msg == 'Change':
      continue
    ret.append('{}님이 {}'.format(dctId[user], tran))

  return ret


record = ['Enter uid1234 Muzi', 'Enter uid4567 Prodo', 'Leave uid1234', 'Enter uid1234 Prodo', 'Change uid4567 Ryan']
result = ['Prodo님이 들어왔습니다.', 'Ryan님이 들어왔습니다.', 'Prodo님이 나갔습니다.', 'Prodo님이 들어왔습니다.']


if __name__ == '__main__':
    ex1 = solution(record)
    print(ex1)
					
