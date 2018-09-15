# ing

def solution(bridge_length, weight, truck_weights):
    
    print("bridge_length : ", bridge_length)
    print("weight        : ", weight)
    print("truck_weights : ", truck_weights)

    wait = 0
    onthebridge = list()

    for truck in truck_weights:
        onthebridge.append(truck)
        
        if len(onthebridge) > bridge_length:
            onthebridge.pop(0)

        if sum(onthebridge) > weight:
            wait += 1

    return len(truck_weights) + bridge_length + wait


bridge_length = [2, 100, 100]
weight        = [10, 100, 100]
truck_weights = [[7, 4, 5, 6],
                 [10],
                 [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]]
result        = [8, 101, 110]


# checker

for i in [0, 1, 2]:
    test = solution(bridge_length[i], weight[i], truck_weights[i])
    print(f'test{i}: {result[i]} == {test} ?', result[i] == test)
    print()

