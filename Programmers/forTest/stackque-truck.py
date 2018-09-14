# ing

def solution(bridge_length, weight, truck_weights):
    return -1


bridge_length = [2, 100, 100]
weight = [10, 100, 100]
truck_weights = [
    [7, 4, 5, 6],
    [10],
    [10, 10, 10, 10, 10, 10, 10, 10, 10, 10],
]


# checker
result = [8, 101, 110]

for i in range(3):
    test = solution(bridge_length[i], weight[i], truck_weights[i])
    print(f'test{i}: {test} == {result[i]} ?')
