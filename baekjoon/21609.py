import sys
from collections import deque 
import math
direction_list = [(-1,0),(0,1),(1,0),(0,-1)]

def find_can_go(y,x, graph_map, isVisited, N, first_value):
    # print("hihi")
    return_list = deque()
    for direction in direction_list:
        new_y = y+direction[0]
        new_x = x+direction[1]
        if(new_y < 0 or new_y >= N):
            continue
        if(new_x < 0 or new_x >=N):
            continue
        if(isVisited[(new_y,new_x)] == True):
            continue
        if(graph_map[new_y][new_x] <= -1):
            continue
        if(graph_map[new_y][new_x] != first_value and first_value != 0 and graph_map[new_y][new_x] != 0):
            continue
        return_list.append((new_y,new_x))
    return return_list

def bfs(y, x, graph_map, N):
    isVisited = dict()
    for y_i in range(N):
        for x_i in range(N):
            isVisited[(y_i,x_i)] = False

    first_row = y
    first_column = x
    first_value = graph_map[y][x]
    go_list = [(y,x)]

    rainbow_count = 0
    if(first_value == 0):
        rainbow_count += 1

    count = 1

    isVisited[(y,x)] = True
    canGoList = deque()
    next_go_list = find_can_go(y,x, graph_map, isVisited, N, first_value)
    canGoList.extend(next_go_list)
    while canGoList:
        nowGo = canGoList.popleft()
        if(first_value != 0 and first_value != graph_map[nowGo[0]][nowGo[1]] and graph_map[nowGo[0]][nowGo[1]] != 0):
            continue
        if(isVisited[nowGo] == True):
            continue
        isVisited[nowGo] = True
        if(first_value == 0):
            first_value = graph_map[nowGo[0]][nowGo[1]]
        if(graph_map[nowGo[0]][nowGo[1]] == 0):
            rainbow_count += 1
        canGoList.extend(find_can_go(nowGo[0],nowGo[1], graph_map, isVisited,N, first_value))
        count += 1
        go_list.append(nowGo)
    return (count, rainbow_count, first_row, first_column, go_list)

def find_biggest_block_group(graph_map,N):
    block_group_list = list()
    for y in range(N):
        for x in range(N):
            if(graph_map[y][x] > -1):
                result = bfs(y, x, graph_map, N)
                if(result[0]>=2):
                    block_group_list.append(result)
    if(len(block_group_list)>0):
        result = sorted(block_group_list, key = lambda x : (-x[0],-x[1],-x[2],-x[3]))
        return result[0]
    else:
        return -1
def gravity(graph_map, N):
    # print("00000000000000 Gravity 0000000000000")
    new_graph_map = list(zip(*graph_map[::-1]))
    for column_index in range(N):
        now_column = new_graph_map[column_index]
        list_of_black = [i for i in range(len(now_column)) if now_column[i] == -1]
        if(len(list_of_black) > 0):
            i = 0
            new_row = list()
            for black_index in list_of_black:
                sliced_row = list(now_column[i:black_index])
                sliced_new_row = [node for node in sliced_row if node > -2]
                sliced_new_row += [-2 for index in range(len(sliced_row)-len(sliced_new_row))]
                new_row += sliced_new_row
                i = black_index
            sliced_row = sliced_row = list(now_column[i:])
            sliced_new_row = [node for node in sliced_row if node > -2]
            sliced_new_row += [-2 for index in range(len(sliced_row)-len(sliced_new_row))]
            new_row += sliced_new_row
            new_graph_map[column_index] = new_row
        else:
            new_row = [node for node in now_column if node > -2]
            new_row += [-2 for index in range(len(now_column)-len(new_row))]
            new_graph_map[column_index] = new_row
    for i in range(3):
        new_graph_map = list(zip(*new_graph_map[::-1]))
    for i in range(len(new_graph_map)):
        new_graph_map[i] = list(new_graph_map[i])
    # print("00000000000000 Gravity 0000000000000")
    return new_graph_map



def solution(graph_map, N, M):
    result = 0
    while True:
        print("========================================\n")
        biggest_block_group = find_biggest_block_group(graph_map,N)
        print("biggest_block_group : ", biggest_block_group)
        print("-------삭제 전---------")
        for i in graph_map:
            print(i)

        if(biggest_block_group == -1):
            break
        delete_list = biggest_block_group[4]
        result += math.floor(math.pow(biggest_block_group[0],2))
        for delete_node in delete_list:
            graph_map[delete_node[0]][delete_node[1]] = -2
        
        print("-------삭제 후---------")
        for i in graph_map:
            print(i)

        graph_map = gravity(graph_map, N)

        print("-------중력 후---------")
        for i in graph_map:
            print(i)


        for spin in range(3):
            graph_map = list(zip(*graph_map[::-1]))
            for i in range(len(graph_map)):
                graph_map[i] = list(graph_map[i])

        print("-------스핀 후---------")
        for i in graph_map:
            print(i)

        graph_map = gravity(graph_map, N)

        print("-------중력 후---------")
        for i in graph_map:
            print(i)
    return result


if __name__ == "__main__":
    N, M = map(int, sys.stdin.readline().split(' '))
    graph_map = [0 for i in range(N)]
    for i in range(N):
        line = [*map(int, sys.stdin.readline().split(' '))]
        graph_map[i] = line
    print(solution(graph_map,N, M))