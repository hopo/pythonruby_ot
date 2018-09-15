# quiz-Chating.py


def solution(record):
  answer = list()
  smpl = list()
  idnick = dict()

  for row in record:
    each = row.split(' ')
    rid = each[1]
    rend = each[0]

    if len(each) == 3:
      rnick = each[2]

    idnick[rid] = rnick
    smpl.append([rid, rend])

  message = ''
  for e in smpl:
    if e[1] == 'Enter':
    	message = '들어왔습니다'
    elif e[1] == 'Leave':
    	message = '나갔습니다'
    elif e[1] == 'Change':
    	continue

    answer.append('{}님이 {}.'.format(idnick[e[0]], message))
  return answer


record = ['Enter uid1234 Muzi', 'Enter uid4567 Prodo', 'Leave uid1234', 'Enter uid1234 Prodo', 'Change uid4567 Ryan']
result = ['Prodo님이 들어왔습니다.', 'Ryan님이 들어왔습니다.', 'Prodo님이 나갔습니다.', 'Prodo님이 들어왔습니다.']


if __name__ == '__main__':
    ex1 = solution(record)
    print(ex1)
					
