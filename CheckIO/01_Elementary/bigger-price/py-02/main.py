
def bigger_price(limit: int, data: list) -> list:
    lst = list()
    cnt = 0
    for i in range(len(data)):
        for j in range(len(data)):
            if (data[i]['price'] < data[j]['price']):
                cnt += 1
        lst.append(cnt)
        cnt = 0

    ret = list()
    for n in range(limit):
        ret.append(data[lst.index(n)])

    return ret


if __name__ == '__main__':
    from pprint import pprint

    ex1 = bigger_price(2,
        [
            {"name": "bread", "price": 100},
            {"name": "wine", "price": 138},
            {"name": "meat", "price": 15},
            {"name": "water", "price": 1}
        ]) # [ {"name": "wine", "price": 138}, {"name": "bread", "price": 100} ], "First"
    pprint(ex1)
    
    ex2 = bigger_price(1,
        [
            {"name": "pen", "price": 5},
            {"name": "whiteboard", "price": 170}
        ]) # [{"name": "whiteboard", "price": 170}], "Second"
    pprint(ex2)
