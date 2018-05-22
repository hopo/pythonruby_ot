
def getMinSum(A,B):
    lst = list()
    for x in A:
        for y in B:
            lst.append(x * y)

    lnth = len(lst)
    ret = list()
    for x in range(lnth//2):
        ret.append(lst[x] + lst[lnth-1-x])
        
    return min(ret)

if __name__ == '__main__':
    print(getMinSum([1,2],[3,4])) # 10
