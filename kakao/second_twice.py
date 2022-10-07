def solution(cap, n, deliveries, pickups):
    answer = -1
    deliverySum = sum(deliveries)
    deliveryIndexs = []
    for i in range(len(deliveries)):
        if deliveries[i] > 0:
            deliveryIndexs.append(i)
    pickupSum = sum(pickups)
    
    while deliverySum+pickupSum > 0:
        departure = 0
        minDel = 0
        toGo = []
        for i in range(len(deliveryIndexs)):
            if(departure + deliveries[deliveryIndexs[i]] <= cap):
                departure += deliveries[deliveryIndexs[i]]
                toGo.append(deliveryIndexs[i])
        nowCap = departure
        answer += n-1
        for i in range(n+1, 0):
            answer += 1
            if(i >= minDel):
                nowCap -= deliveries[i]
                deliveries[i] -= deliveries[i]
            else:
                
    print(deliveries)
    now = 0
    
        
    return answer

if __name__ == '__main__':
    cap = 4
    n = 5
    deliveries = [1, 0, 3, 1, 2]
    pickups =  [0, 3, 0, 4, 0]
    print(solution(cap, n, deliveries, pickups))