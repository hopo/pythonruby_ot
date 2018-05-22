
def productMatrix(A, B):
    ret = [[0,0],[0,0]]
    for i in range(len(A)):
        for j in range(len(a[0])):
            ret[i][j] = (A[i][0] * B[0][j]) + (A[i][1] * B[1][j])
    return ret

if __name__ == '__main__':
    a = [[1, 2], [2, 3]]
    b = [[3, 4], [5, 6]]
    ex = productMatrix(a, b) # [[13, 16], [21, 26]]
    print(ex)

