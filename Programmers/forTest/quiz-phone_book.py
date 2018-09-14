
def solution(phone_book):
    x = sorted(phone_book)
    print(x[0])
    print(len(x[1]))
    print(x[1].split('ss'))
    print(len(x[1]))

    return ''


pbook01 = ['119', '97674223', '1195524421']
ret01 = solution(pbook01)
print(ret01)  # False

'''
pbook02 = ['123', '456', '789']
ret02 = solution(pbook02)
print(ret02)  # True

pbook03 = ['12', '123', '1235', '567', '88']
ret03 = solution(pbook03)
print(ret03)  # False
'''
