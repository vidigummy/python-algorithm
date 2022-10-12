import sys
import math
from collections import deque
direction_list = [(1,0),(-1,0),(0,1),(0,-1)]


def bfs(graph_map, now_geo, isVisited):
    can_go_list = deque()
    cnt = 1
    isVisited[now_geo] = True
    for direction in direction_list:
        next_yx = (now_geo[0]+direction[0], now_geo[1]+direction[1])
        if next_yx in graph_map and isVisited[next_yx] == False and graph_map[next_yx] > 0:
            can_go_list.append(next_yx)
    while can_go_list:
        now_geo = can_go_list.popleft()
        if(isVisited[now_geo] == False):
            isVisited[now_geo] = True
            for direction in direction_list:
                next_yx = (now_geo[0]+direction[0], now_geo[1]+direction[1])
                if next_yx in graph_map and isVisited[next_yx] == False and graph_map[next_yx] > 0:
                    can_go_list.append(next_yx)
            cnt += 1
    if cnt < 2:
        return 0, isVisited
    return cnt, isVisited


def check_three_ice(graph_map,now_geo, max):
    count = 0
    for direction in direction_list:
        next_y = now_geo[0]+direction[0]
        next_x = now_geo[1]+direction[1]
        if ((next_y,next_x) in graph_map and next_y < max and next_x < max):
            if(graph_map[(next_y,next_x)] > 0):
                count += 1
    if(count < 3):
        return False
    return True


def solution(N,Q,graph_map,magic_list,isVisited):
    max = math.floor(math.pow(2,N))
    for magic in magic_list:
        square_len = math.floor(math.pow(2,magic))
        # 반바퀴 돌려뿌기~
        for y_start in range(max//square_len):
            smallest = y_start*square_len
            biggest = smallest+square_len
            for i in range(smallest,biggest):
                for j in range(i,biggest):
                    tmp = graph_map[(i,j)]
                    graph_map[(i,j)] = graph_map[(j,i)]
                    graph_map[(j,i)] = tmp
        # 얼음 있는 칸 체크~
        del_list = deque()
        for geo in graph_map.keys():
            if(graph_map[geo] > 0):
                if(check_three_ice(graph_map,geo,max) == False):
                    del_list.append(geo)
        for del_yx in del_list:
            graph_map[del_yx] -= 1
    # 남아있는 얼음 양
    ice_sum = 0
    for geo in graph_map.keys():
        ice_sum += graph_map[geo]
    # bfs 돌릴 시간
    max = 0
    
    for geo in graph_map.keys():
        if isVisited[geo] == False:
            tmp, isVisited = bfs(graph_map,geo,isVisited)
            if tmp > max:
                max = tmp
    
    return ice_sum, max

                
        

if __name__ == '__main__':
    N, Q = map(int, sys.stdin.readline().split(' '))
    graph_map = dict()
    isVisited = dict()
    for y in range(int(pow(2,N))):
        line = [*map(int,sys.stdin.readline().split(' '))]
        for x in range(len(line)):
            graph_map[(y,x)] = line[x]
            isVisited[(y,x)] = False
    magic_list= [*map(int,sys.stdin.readline().split(' '))]
    ice_sum, max = solution(N,Q,graph_map,magic_list,isVisited)
    print(ice_sum)
    print(max)
