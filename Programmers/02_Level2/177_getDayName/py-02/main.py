
def getDayName(a,b):
    yoil = ['SUN','MON','TUE','WED','THU','FRI','SAT']
    ldays = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    td = yoil.index('FRI')-1 + sum(ldays[:a-1]) + b

    return yoil[td%7]

if __name__ == '__main__':
    print(getDayName(1,1)) # FRI
    print(getDayName(5,24)) # TUE
