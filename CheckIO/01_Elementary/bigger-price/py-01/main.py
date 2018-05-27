# https://py.checkio.org/mission/bigger-price/solve/

"""
You have a table with all available goods in the store. The data is represented as a list of dicts
Your mission here is to find the TOP most expensive goods. The amount we are looking for will be given as a first argument and the whole data as the second one
Input: int and list of dicts. Each dicts has two keys "name" and "price"
Output: the same as the second Input argument.
"""

def bigger_price(limit: int, data: list) -> list:
    return data


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

