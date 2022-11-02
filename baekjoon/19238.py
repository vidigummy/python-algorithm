import sys
from collections import deque
direction_list = [(-1,0),(1,0),(0,-1),(0,1)]

def find_next_direction_list(graph_map, N, now_y, now_x, isVisited):
    can_go_list = deque()
    for direction in direction_list:
        next_y = now_y + direction[0]
        next_x = now_x + direction[1]
        if next_y <= 0 or next_y > N or next_x <= 0 or next_x >N or graph_map[next_y][next_x] == 1 or (next_y, next_x) in isVisited:
            continue
        else:
            can_go_list.append((next_y, next_x))
    return can_go_list


def find_destination(graph_map,now_geo, N, destination):
    depth =0
    if now_geo == destination:
        return depth
    isVisited = dict()
    isVisited[now_geo] = True
    can_go_list = find_next_direction_list(graph_map,N,now_geo[0],now_geo[1], isVisited)
    while True:
        new_can_go_list = deque()
        depth += 1
        while can_go_list:
            go = can_go_list.popleft()
            isVisited[go] = True
            if go == destination:
                return depth
            can_go = find_next_direction_list(graph_map,N,go[0],go[1], isVisited)
            new_can_go_list = new_can_go_list + can_go
        can_go_list = new_can_go_list


def find_passenger(graph_map, passenger_map, now_geo, N):
    depth =0
    if now_geo in passenger_map:
        return (depth,now_geo)
    isVisited = dict()
    isVisited[now_geo] = True
    can_go_list = find_next_direction_list(graph_map,N,now_geo[0],now_geo[1], isVisited)
    while True:
        new_can_go_list = deque()
        depth += 1
        while dict([can_go_list].sort(key = lambda x: (x[0],x[1]))):
            go = can_go_list.popleft()
            isVisited[go] = True
            if go in passenger_map:
                return (depth,go)
            can_go = find_next_direction_list(graph_map,N,go[0],go[1], isVisited)
            new_can_go_list = new_can_go_list + can_go
        can_go_list = new_can_go_list
        if(len(can_go_list) < 1):
            return False


def solution(graph_map, passenger_map, N, M, F, start_y, start_x):
    answer = False
    while F > 0:
        # 태울 승객을 고르기.
        # print("----------------------------------------")
        # print("now F : ", F)
        find_next_passenger = find_passenger(graph_map,passenger_map,(start_y,start_x),N)
        if(find_next_passenger == False):
            return -1
        next_passenger_geo = find_next_passenger[1]
        using_fuel = 0
        F -= find_next_passenger[0]
        # print("find_next_passenger : ", find_next_passenger)
        # 승객이 타고 나서 사용하게 될 연료 구하기
        passengers_destination = passenger_map[next_passenger_geo]
        using_fuel += find_destination(graph_map,next_passenger_geo,N, passengers_destination)
        # print("using_fuel : ", using_fuel)
        # 만약 사용해야할 연료량이 F보다 많으면 운행 종료여
        if(using_fuel > F):
            break
        # 아니라면 연료량 줄여주기
        else:
            F += using_fuel
        # 그리고 그 승객은 없어지겠지?
        del passenger_map[next_passenger_geo]
        # 만약 승객이 더 없다면.
        if len(passenger_map.keys()) == 0:
            answer = F
            break
        start_y = passengers_destination[0]
        start_x = passengers_destination[1]

    if answer == False:
        return -1
    else:
        return answer


if __name__ == '__main__':
    N, M, F = map(int, sys.stdin.readline().split(' '))
    graph_map = [1 for i in range(N+1)]
    passenger_map = dict()
    for i in range(1,N+1):
        line = [*map(int, sys.stdin.readline().split(' '))]
        graph_map[i] = [1]
        graph_map[i] += line
    start_y, start_x = map(int, sys.stdin.readline().split(' '))
    for i in range(M):
        passanger_y, passanger_x, destination_y, destination_x = map(int, sys.stdin.readline().split(' '))
        passenger_map[(passanger_y, passanger_x)] = (destination_y, destination_x)
    print(solution(graph_map,passenger_map,N,M,F, start_y, start_x))