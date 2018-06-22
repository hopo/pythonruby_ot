
def getDayName(a,b):
    yoil = ['SUN','MON','TUE','WED','THU','FRI','SAT']
    ldays = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    td = 4
    for d in range(a-1):
        td += ldays[d]
    td += b

    return yoil[td%7]

if __name__ == '__main__':
    print(getDayName(1,1)) # FRI
    print(getDayName(5,24)) # TUE
