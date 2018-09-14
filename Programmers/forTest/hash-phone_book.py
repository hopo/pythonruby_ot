# ===============
# Phone Book
# ===============

def solution(phone_book):
    sample = sorted(phone_book)

    for i in range(1, len(sample)):
        if sample[i] != sample[i].split(sample[i-1])[0]:
            return False
    return True

# others
'''
def solution(phoneBook):
    phoneBook = sorted(phoneBook)

    for p1, p2 in zip(phoneBook, phoneBook[1:]):
        if p2.startswith(p1):
            return False
    return True
'''


pbook01 = ['119', '97674223', '1195524421']
ret01 = solution(pbook01)
print(ret01)  # False

pbook02 = ['123', '456', '789']
ret02 = solution(pbook02)
print(ret02)  # True

pbook03 = ['12', '123', '1235', '567', '88']
ret03 = solution(pbook03)
print(ret03)  # False
