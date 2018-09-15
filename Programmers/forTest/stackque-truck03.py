# ing


def solution(bridge_length, weight, truck_weights):
    
    print("bridge_length : ", bridge_length)
    print("weight        : ", weight)
    print("truck_weights : ", truck_weights)

    ret = (bridge_length + 1)

    onbridge = 0
    wait = 0
    time = 0
    i = 0
    cnt = 0

    for tw in truck_weights:
        time += 1
        if onbridge > weight:
            wait += 1
        else:
            onbridge += tw
            cnt += 1

        if cnt > bridge_length:
            cnt = 0
            onbridge -= truck_weights[i]
            i += 1

    return ret + time + wait


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

