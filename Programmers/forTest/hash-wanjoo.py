# ===============
# Wan Joo Man
# ===============

# my01
def solution(pati, comp):
    
    pa = sorted(pati)
    co = sorted(comp)
    clen = len(co)
    plen = len(pa)

    for i in range(clen):
        if pa[i] != co[i]:
            return pa[i]

    return pa[plen-1]


# others
'''
import collections
def solution(pati, comp):
    pati_cnt = collections.Counter(pati)
    comp_cnt = collections.Counter(comp)
    answer = pati_cnt - comp_cnt
    #print(f'P: {pati_cnt}\nC: {comp_cnt}')
    #print(f'answer: {answer}')
    
    return list(answer.keys())[0]
'''


# check below
pati01 = ['leo', 'kiki', 'eden']
comp01 = ['kiki', 'eden']
ret01 = solution(pati01, comp01)
print(ret01)    # leo

pati02 = ['ma', 'jo', 'ni', 'vin', 'fil']
comp02 = ['ma', 'jo', 'ni', 'fil']
ret02 = solution(pati02, comp02)
print(ret02)    # vin

pati03 = ['mis', 'stan', 'mis', 'ana']
comp03 = ['stan', 'mis', 'ana']
ret03 = solution(pati03, comp03)
print(ret03)    # mis
