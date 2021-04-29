def solution(bridge_length, weight, truck_weights):
    bridge = [0]*bridge_length
    time = 0
    finished = []
    sum_weights = sum(truck_weights)
    while sum_weights!=sum(finished):
        time+=1
        finished.append(bridge.pop(0))

        if len(truck_weights)>0:
            bridge.append(truck_weights.pop(0))

        if sum(bridge)>weight:
            truck_weights.insert(0,bridge.pop())
            bridge.append(0)



    return time
