
def bigger_price(limit: int, data: list) -> list:
    lnth = len(data)
    for i in range(lnth-1):
        for j in range(i, lnth):
            if data[i]['price'] < data[j]['price']:
                data[i], data[j] = data[j], data[i]
    return data[:limit]


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

