import sys
import math
from collections import deque as dq
direction_list = [(1,0),(-1,0),(0,1),(0,-1)]
def check_go(graph_map, now_y, now_x, max, isVisited):
    can_go_list = dq()
    for direction in direction_list:
        next_y = now_y+direction[0]
        next_x = now_x+direction[1]
        if (next_y >= 0 and next_x >= 0 and next_y < max and next_x < max and graph_map[next_y][next_x] > 0 and isVisited[(next_y,next_x)] == False):
            can_go_list.append((next_y, next_x))
    return can_go_list

def bfs(start_y, start_x, graph_map, isVisited, max):
    count = 1
    can_go_list = check_go(graph_map, start_y, start_x, max, isVisited)
    isVisited[(start_y, start_x)] = True
    while can_go_list:
        now_go = can_go_list.popleft()
        if(isVisited[now_go] == False):
            isVisited[now_go] = True
            can_go_list.extend(check_go(graph_map,now_go[0],now_go[1], max, isVisited))
            count += 1
    if(count < 2):
        return 0, isVisited
    return count, isVisited

def check_three_ice(graph_map,now_y,now_x, max):
    count = 0
    for direction in direction_list:
        next_y = now_y+direction[0]
        next_x = now_x+direction[1]
        if (next_y >= 0 and next_x >= 0 and next_y < max and next_x < max):
            if(graph_map[next_y][next_x] > 0):
                count += 1
    if(count < 3):
        return False
    return True
def solution(N,Q,graph_map,magic_list):
    graph_len = len(graph_map)
    isVisited = dict()
    for i in range(Q):
        L = magic_list[i]
        two_pow_l = math.floor((math.pow(2,L)))
        # 모든 격자를 시계 방향으로 90도 회전하기 ok debug완료
        for y_index in range(math.floor(graph_len/two_pow_l)):
            for x_index in range(math.floor(graph_len/two_pow_l)):
                y = y_index*two_pow_l
                x = x_index*two_pow_l
                square = [graph_map[i][x:x+two_pow_l] for i in range(y,y+two_pow_l)]
                square = list(map(list,zip(*square[::-1])))
                for small_y in range(y, y+two_pow_l):
                    for small_x in range(x, x+two_pow_l):
                        graph_map[small_y][small_x] = square[small_y-y][small_x-x]
        # 주변에 얼음 있는 칸이 3개 이상인지 확인하여 줄이기.
        del_list = dq()
        for y in range(graph_len):
            for x in range(graph_len):
                isVisited[(y,x)] = False
                if(check_three_ice(graph_map, y, x, graph_len) == False):
                    del_list.append((y,x))
        while del_list:
            del_yx = del_list.popleft()
            if(graph_map[del_yx[0]][del_yx[1]]>0):
                graph_map[del_yx[0]][del_yx[1]] -= 1
    # 남아있는 얼음의 합
    sum_of_ice = 0
    for row in graph_map:
        sum_of_ice += sum(row)
    # 남아있는 얼음 중, 가장 큰 덩어리가 차지하는칸의 개수
    max = 0
    for y in range(graph_len):
        for x in range(graph_len):
            if(isVisited[(y,x)]==False and graph_map[y][x] > 0):
                tmp, isVisited = bfs(y,x,graph_map,isVisited, graph_len)
                if(tmp > max):
                    max = tmp
    return sum_of_ice, max

if __name__ == '__main__':
    N, Q = map(int, sys.stdin.readline().split(' '))
    graph_map = [0 for i in range(int(pow(2,N)))]
    for i in range(int(pow(2,N))):
        graph_map[i] = [*map(int,sys.stdin.readline().split(' '))]
    magic_list= [*map(int,sys.stdin.readline().split(' '))]
    sum, max = solution(N,Q,graph_map,magic_list)
    print(sum)
    print(max)
