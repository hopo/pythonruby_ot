import csv
import re

from pprint import pprint

def runcode():
    rslt = []
    with open('entrypoint.py') as f:
        for ln in f.readlines():
            if re.search('url\(', ln):
                aa = ln.split('url(')[1]
                x = aa.split(',')[0]
                try:
                    bb = ln.split('name=')[1]
                    y = bb.split(')')[0]
                except:
                    y = 'NONE'
                #data = {'x':x, 'y':y}
                data = (x, y)
                rslt.append(data)

    return rslt

def runcode_2nd():
    rslt = []
    with open('entrypoint.py') as f:
        for ln in f.readlines():
            if re.search('url\(', ln):
                first = ln.split('url(')[1]
                second = first.split(',')
                aa = second[0]
                bb = second[1]
                cc = second[2]

                if re.search('as_view', bb):
                    bb = bb.split('.')[0]

                if re.search('name=', cc):
                    cc = cc.split('name=')[1]
                    cc = cc.split(")")[0]
                else:
                    cc = '-'

                rslt.append((aa, bb, cc))
    return rslt
    


def listtocsv(datalist):
    with open('output.csv', 'w') as f:
        wr = csv.writer(f, dialect='excel')
        wr.writerows(datalist)
    print('Write CSV Done!')


if __name__ == '__main__':
    r = runcode_2nd()
    listtocsv(r)
