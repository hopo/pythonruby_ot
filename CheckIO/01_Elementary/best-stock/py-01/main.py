
def best_stock(data):
    lstkeys = list(data.keys())
    lstvals = list(data.values())
    mx = max(lstvals)
    mxidx = lstvals.index(mx)
    return lstkeys[mxidx]

if __name__ == '__main__':
    ex1 = best_stock({ 'CAC': 10.0, 'ATX': 390.2, 'WIG': 1.2 }) # 'ATX', "First"
    print(ex1)
    ex2 = best_stock({ 'CAC': 91.1, 'ATX': 1.01, 'TASI': 120.9 }) # 'TASI', "Second"
    print(ex2)
