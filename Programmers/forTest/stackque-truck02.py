# ing


def solution(bridge_length, weight, truck_weights):
    
    print("bridge_length : ", bridge_length)
    print("weight        : ", weight)
    print("truck_weights : ", truck_weights)

    onbridge = list()
    cnt = 0

    for w in truck_weights:

        onbridge.append(w)
        if sum(onbridge) > weight:
            cnt += 1

        if len(onbridge) == bridge_length:
            onbridge.pop(0)

    ret = len(truck_weights)*bridge_length + bridge_length - cnt

    return ret


bridge_length = [2, 100, 100]
weight        = [10, 100, 100]
truck_weights = [[7, 4, 5, 6],
                 [10],
                 [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]]
result        = [8, 101, 110]


# checker

for i in range(2, 3):
    test = solution(bridge_length[i], weight[i], truck_weights[i])
    print(f'test{i}: {result[i]} == {test} ?', result[i] == test)
    print()
