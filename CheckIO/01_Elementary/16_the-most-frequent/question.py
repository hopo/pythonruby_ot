
def most_frequent(data):
    data.sort()
    target = data[0]
    most = data[0]
    mx = 0
    cnt = 0
    for i in range(len(data)):
        if target != data[i]:
            if cnt > mx:
                most = data[i-1]
                mx = cnt
                cnt = 1
        cnt += 1
    return most

if __name__ == '__main__':
    ex1 = most_frequent(['a', 'b', 'c', 'a', 'b', 'a']) # 'a'
    print(ex1)
    ex2 = most_frequent(['a', 'a', 'bi', 'bi', 'bi']) # 'bi'
    print(ex2)
