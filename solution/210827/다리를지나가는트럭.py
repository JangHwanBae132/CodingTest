from collections import deque

def solution(bridge_length, weight, truck_weights):
    answer = 0
    truck = deque(truck_weights)

    total_weight = truck[0]
    bridge = deque()
    bridge.append([0, truck.popleft()])
    while bridge:
        answer += 1
        if answer-bridge[0][0] > bridge_length:
            passed_truck = bridge.popleft()
            total_weight += -passed_truck[1]
        if len(truck) != 0 and len(bridge) <= bridge_length and total_weight+truck[0] <= weight:
            new_truck = truck.popleft()
            bridge.append([answer-1, new_truck])
            total_weight += new_truck
    #     print(total_weight)
    #     print(bridge)
    # print(answer)
    return answer
