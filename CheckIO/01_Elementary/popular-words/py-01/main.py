
def popular_words(text: str, words: list) -> dict:
    rt = text.replace('\n', ' ')

    spl = rt.lower().split(' ')
    ls = list()
    for e in spl:
        if e[-1:] == '\n':
            e = e[:-1]
        if e != '':
            ls.append(e)
            
    ret = dict()
    for w in words:
        cnt = 0
        for e in ls:
            if w == e:
                cnt += 1
        ret[w] = cnt
        
    return ret


if __name__ == '__main__':
    ex1 = popular_words(
'''
When I was One
I had just begun
When I was Two
I was nearly new
''', 
        ['i', 'was', 'three', 'near']) # { 'i': 4, 'was': 3, 'three': 0, 'near': 0 }
    print(ex1)

