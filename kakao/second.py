def dfs(now, nowCap, maxCap, deliveries, pickups, cnt, n):
    print(now, nowCap, maxCap, deliveries, pickups, cnt, n)
    if sum(deliveries) ==0 and sum(pickups) ==0:
        print("done")
        if now == 0:
            return cnt
        else:
            return cnt+now
    else:
        if now == 0:
            for i in range(0, maxCap):
                return dfs(1, [i,0], maxCap, deliveries, pickups, 1, n)
        else:
            dfsResults = []
            if deliveries[now-1]>0:
                print("deliveries -> pickups")
                print(deliveries[now-1], nowCap[0]> deliveries[now-1] , nowCap[0])
                for j in range(0, nowCap[0] if nowCap[0]> deliveries[now-1] else deliveries[now-1]):
                    if pickups[now-1]>0:
                        print(pickups[now-1] , maxCap-(sum(nowCap)-j) > pickups[now-1] , maxCap-(sum(nowCap)-j))
                        for i in range(0,  maxCap-(sum(nowCap)-j) if maxCap-(sum(nowCap)-j) > pickups[now-1] else pickups[now-1]):
                            newDeliveries = deliveries
                            newDeliveries[now-1] -= j
                            newPickups = pickups
                            newPickups[now-1] -= i
                            dfsResults.append(dfs(now-1, [nowCap[0]-j,nowCap[1]+i], maxCap, newDeliveries, newPickups, cnt+1, n))
                            if(now+1 != n):
                                dfsResults.append(dfs(now+1, [nowCap[0]-j,nowCap[1]+i], maxCap, newDeliveries, newPickups, cnt+1, n))
                    else:
                        print("deliver!")
                        newDeliveries = deliveries
                        newDeliveries[now-1] -= j
                        dfsResults.append(dfs(now-1, [nowCap[0]-j,nowCap[1]], maxCap, newDeliveries, pickups, cnt+1, n))
                        if(now+1 != n):
                            dfsResults.append(dfs(now+1, [nowCap[0]-j,nowCap[1]], maxCap, newDeliveries, pickups, cnt+1, n))
            elif pickups[now-1]>0:
                print("pickups")
                for i in range(0, pickups[now-1] if maxCap-(sum(nowCap)) > pickups[now-1] else maxCap-(sum(nowCap))):
                    newPickups = pickups
                    newPickups[now-1] -= i
                    dfsResults.append(dfs(now-1, [nowCap[0], nowCap[1]+i], maxCap, deliveries, newPickups, cnt+1, n))
                    if(now+1 != n):
                        dfsResults.append(dfs(now+1, [nowCap[0], nowCap[1]+i], maxCap, deliveries, newPickups, cnt+1, n))
            else:
                print("nothingHere")
                dfsResults.append(dfs(now-1, nowCap, maxCap, deliveries, pickups, cnt+1, n))
                if(now+1 != n):
                    dfsResults.append(dfs(now+1, nowCap, maxCap, deliveries, pickups, cnt+1, n))
            print(dfsResults)
            return min(dfsResults)
                        

            
def solution(cap, n, deliveries, pickups):
    answer = -1
    nowCap = [0,0]
    answer = dfs(0, [0,0], cap, deliveries, pickups, 0, n)
    print(answer)
    now = 0
    
        
    return answer

if __name__ == '__main__':
    cap = 4
    n = 5
    deliveries = [1, 0, 3, 1, 2]
    pickups =  [0, 3, 0, 4, 0]
    print(solution(cap, n, deliveries, pickups))