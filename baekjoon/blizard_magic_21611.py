import sys
import math
def make_map(graph, S_y, S_x):
    newMapList = list()
    new_map = dict()
    # left는 0, right는 1로 처리한다.
    now_step = 1
    # 하-우 // 상-좌
    flag = 0
    # start point
    now_y = S_y
    now_x = S_x-1
    prev = (S_y,S_x)
    while not( now_y == 0 and now_x == 0 ):
        if flag == 0:
            # 첫 시작
            next_y = now_y-now_step
            for i in range(now_y-1, next_y, -1):
                next_node = (i-1, now_x)
                new_map[(i,now_x)] = [prev, next_node]
                prev = (i,now_x)
            flag = 1
            now_step += 2
            now_y = next_y
        # 우-상 시키기
        if flag == 1:
            next_x = now_x + now_step
            for i in range(now_x, next_x):
                next_node = (now_y, i+1)
                new_map[(now_y, i)] = (prev, next_node)
                prev = (now_y, i)
            now_x = next_x
            next_y = now_y + now_step
            for i in range(now_y, next_y):
                next_node = (i+1, now_x)
                new_map[(i, now_x)] = (prev, next_node)
                prev = (i,now_x)
            now_y = next_y
            flag = 2
        if flag == 2:
            next_x = now_x - now_step
            for i in range(now_x, next_x, -1):
                next_node = (now_y, i-1)
                new_map[(now_y, i)] = (prev, next_node)
                prev = (now_y, i)
            now_x = next_x
            next_y = now_y - now_step
            for i in range(now_y, next_y, -1):
                next_node = (i-1, now_x)
                new_map[(i, now_x)] = (prev, next_node)
                prev = (i, now_x)
            now_y = next_y
            flag = 1






def blizard_magic(graph, magic_direction, magic_length, S_y, S_x):
    if(magic_direction == 2):
        for i in range(S_y, S_y+magic_length+1):
            graph[i][S_x] = 0
    if(magic_direction == 1):
        for i in range(S_y, S_y-magic_length-2, -1):
            graph[i][S_x] = 0
    if(magic_direction == 3):
        for i in range(S_x, S_x-magic_length-2, -1):
            graph[S_y][i] = 0
    if(magic_direction == 4):
        for i in range(S_x, S_x+magic_length+1):
            graph[S_y][i] = 0
    return graph
    

def practice_magic(graph, N, M, S_y, S_x, magic_list):
    while magic_list:
        magic = magic_list.pop(0)
        # 얼음 파편 던지는 상어
        magic_direction = magic[0]
        magic_length = magic[1]
        graph = blizard_magic(graph, magic_direction, magic_length, S_y, S_x,)
        for i in graph:
            print(i)

        # compact

        # 4개 이상의 구슬이 터지는 과정

        # compact

        #구슬이 변하는 과정

    return 0

if __name__ == '__main__':
    N, M  = map(int, sys.stdin.readline().split(" "))
    graph = [0 for i in range(N)]
    for i in range(N):
        tmp = [*map(int, sys.stdin.readline().split(" "))]
        graph[i] = tmp
    S_y = math.floor((N+1)/2)-1
    S_x = math.floor((N+1)/2)-1
    magic_list = [0 for i in range(M)]
    for i in range(M):
        tmp = [*map(int, sys.stdin.readline().split(" "))]
        magic_list[i] = tmp

    print(practice_magic(graph,N,M,S_y,S_x,magic_list))