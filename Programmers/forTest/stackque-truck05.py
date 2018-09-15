# ing

def solution(bridge_length, weight, truck_weights):
    
    print("bridge_length : ", bridge_length)
    print("weight        : ", weight)
    print("truck_weights : ", truck_weights)

    time = 0
    wait = 0
    t = 0
    onBridge = list()

    while t != len(truck_weights):
        time += 1

        if time % bridge_length == 0:
            onBridge.pop(0)

        if sum(onBridge) > weight:
            wait += 1
        else:
            onBridge.append(truck_weights[t])
            t += 1

        print(onBridge)
        print("wait: ", wait)

    return time + wait


bridge_length = [2, 100, 100]
weight        = [10, 100, 100]
truck_weights = [[7, 4, 5, 6],
                 [10],
                 [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]]
result        = [8, 101, 110]


# checker

for i in [0]:
    test = solution(bridge_length[i], weight[i], truck_weights[i])
    print(f'test{i}: {result[i]} == {test} ?', result[i] == test)
    print()

