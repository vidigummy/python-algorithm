import sys
import math
direction_list = [(0,-1),(1,0),(0,1),(-1,0)]
direction_magic_list = [
(((-1,-1),0.1),((-1,0),0.07),((-1,1),0.01),((-2,0),0.02),((1,-1),0.1),((1,-0),0.07),((1,1),0.01),((2,0),0.02),((0,-2),0.05),((0,-1),0.55)),
(((2,0),0.05),((1,1),0.1),((1,-1),0.1),((0,2),0.02),((0,1),0.07),((0,-1),0.07),((0,-2),0.02),((-1,1),0.01),((-1,-1),0.01),((1,0),0.55)),
(((0,2),0.05),((1,1),0.1),((-1,1),0.1),((2,0),0.02),((1,0),0.07),((-1,0),0.07),((-2,0),0.02),((-1,-1),0.01),((1,-1),0.01),((0,1),0.55)),
(((-2,0),0.05),((-1,1),0.1),((-1,-1),0.1),((0,2),0.02),((0,1),0.07),((0,-1),0.07),((0,-2),0.02),((1,-1),0.01),((1,1),0.01),((-1,0),0.55))
]
def wind(graph_map, direction, now_geo):
    score = 0
    magic_map = direction_magic_list[direction]
    now_sand = graph_map[now_geo]
    for magic in magic_map:
        next_y = now_geo[0]+magic[0][0]
        next_x = now_geo[1]+magic[0][1]
        if(magic[1] != 0.55):
            sand_amount = math.floor(now_sand*magic[1])
            graph_map[now_geo] -= sand_amount
            if((next_y,next_x) not in graph_map):
                score += sand_amount
            else:
                graph_map[(next_y,next_x)] += sand_amount
        else:
            sand_amount = graph_map[now_geo]
            if((next_y,next_x) not in graph_map):
                score += sand_amount
            else:
                graph_map[(next_y,next_x)] += sand_amount
    graph_map[now_geo] = 0
    return graph_map, score

def solution(N, graph_map):
    result = 0
    now_geo = (N//2,N//2)
    direction_index = 0
    step = 1
    while (now_geo != (0,0)):
        for x in range(step):
                next_geo = (now_geo[0]+direction_list[direction_index][0], now_geo[1]+direction_list[direction_index][1])
                graph_map, new_score = wind(graph_map, direction_index, next_geo)
                result += new_score
                now_geo = next_geo
                if(next_geo == (0,0)):
                    now_geo = next_geo
                    break
        if(direction_index == 1 or direction_index == 3):
            step += 1
        direction_index = (direction_index + 1)%4
    return result

if __name__ == '__main__':
    N = int(input())
    graph_map = dict()
    for i in range(N):
        tmp_list = [*map(int, sys.stdin.readline().split(' '))]
        for j in range(N):
            graph_map[(i,j)] = tmp_list[j]
    print(solution(N,graph_map))
