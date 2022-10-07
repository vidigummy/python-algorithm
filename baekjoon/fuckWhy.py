from copy import deepcopy
from itertools import product
import sys

dxy = [(0,-1),(-1,-1),(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1)]
d_xy_shark = [1,2,3,4]
d_xy_shark_g = [(-1,0),(0,-1),(1,0),(0,1)]
def fishMoveCheck(fish_geo, fish_direction, shark_map, S_y, S_x,):
    new_fish_direction = fish_direction-1
    for i in range(8):
        next_geo_y = fish_geo[0]+dxy[(new_fish_direction)%8][0]
        next_geo_x = fish_geo[1]+dxy[(new_fish_direction)%8][1]
        if not (next_geo_y == S_y and next_geo_x == S_x):
            if not(next_geo_y < 1 or next_geo_x < 1):
                if not(next_geo_y > 4 or next_geo_x > 4):
                    if not(shark_map[next_geo_y][next_geo_x] > 0):
                        return (next_geo_y, next_geo_x, (new_fish_direction)%8+1)
        new_fish_direction -= 1
    return -1

def move_shark(fishes, shark_map, S_y,S_x):
    max_eat = -1
    max_go_go = []
    max_del_list = []
    nPr = product(d_xy_shark, repeat = 3)
    for goGoShark in nPr:
        # print("----now ",goGoShark,"--------")
        del_list = []
        visit = dict()
        eat_cnt = 0
        next_geo_y = S_y + d_xy_shark_g[goGoShark[0]-1][0]
        next_geo_x = S_x + d_xy_shark_g[goGoShark[0]-1][1]
        if not(next_geo_y < 1 or next_geo_x < 1) and not(next_geo_y > 4 or next_geo_x > 4):
            if (next_geo_y, next_geo_x) in fishes:
                # print("eat += ", len(fishes[(next_geo_y, next_geo_x)]), " at ", (next_geo_y, next_geo_x))
                eat_cnt += len(fishes[(next_geo_y, next_geo_x)])
                # print(eat_cnt)
                del_list.append((next_geo_y, next_geo_x))
                visit[(next_geo_y, next_geo_x)] = 1
        else:
            # print("nope")
            continue
        # 두번째 움직이기
        next_geo_y = next_geo_y + d_xy_shark_g[goGoShark[1]-1][0]
        next_geo_x = next_geo_x + d_xy_shark_g[goGoShark[1]-1][1]
        if not(next_geo_y < 1 or next_geo_x < 1) and not(next_geo_y > 4 or next_geo_x > 4):
            if (next_geo_y, next_geo_x) in fishes and not (next_geo_y, next_geo_x) in visit:
                # print("eat : ", len(fishes[(next_geo_y, next_geo_x)]), " at ", (next_geo_y, next_geo_x))
                eat_cnt += len(fishes[(next_geo_y, next_geo_x)])
                # print(eat_cnt)
                del_list.append((next_geo_y, next_geo_x))
                visit[(next_geo_y, next_geo_x)] = 1
        else:
            # print("nope")
            continue
        # 세번째 움직이기
        next_geo_y = next_geo_y + d_xy_shark_g[goGoShark[2]-1][0]
        next_geo_x = next_geo_x + d_xy_shark_g[goGoShark[2]-1][1]
        if not(next_geo_y < 1 or next_geo_x < 1) and not(next_geo_y > 4 or next_geo_x > 4):
            if (next_geo_y, next_geo_x) in fishes and not (next_geo_y, next_geo_x) in visit:
                # print("eat : ", len(fishes[(next_geo_y, next_geo_x)]), " at ", (next_geo_y, next_geo_x))
                eat_cnt += len(fishes[(next_geo_y, next_geo_x)])
                # print(eat_cnt)
                del_list.append((next_geo_y, next_geo_x))
                visit[(next_geo_y, next_geo_x)] = 1
        else:
            # print("nope")
            continue
        # print(eat_cnt)
        if eat_cnt > max_eat:
            max_eat = eat_cnt
            max_del_list = del_list
            max_go_go = (next_geo_y, next_geo_x)
    # print(max_eat)
    for i in max_del_list:
        del(fishes[i])
        shark_map[i[0]][i[1]] = 3
    return shark_map, fishes, max_go_go


def show_magic(shark_map, fishes, S_y, S_x, S, M):
    
    for magic in range(S):
        # print("============\nmagic : ",magic+1)
        
        # 마법 시작 (1)
        duplicate_magic = deepcopy(fishes)
        # 물고기 이동(2)(이동 가능한지 체크, 어디로 이동 가능한지 체크 후 이동)
        fishes_new = dict()
        # print("이동 전")
        for fish_geo in fishes.keys():
            fishList = fishes[fish_geo]
            fishLen = len(fishList)
            # print("**************")
            for i in range(fishLen):
                # print(fishList)
                fish_d = fishList.pop(0)
                fishRouteCheckResult =  fishMoveCheck(fish_geo, fish_d, shark_map, S_y, S_x)
                if fishRouteCheckResult != -1:
                    if ((fishRouteCheckResult[0],fishRouteCheckResult[1])) in fishes_new:
                        tmpList = fishes_new[(fishRouteCheckResult[0],fishRouteCheckResult[1])]
                        tmpList.append(fishRouteCheckResult[2])
                        fishes_new[(fishRouteCheckResult[0],fishRouteCheckResult[1])] = tmpList
                    else:
                        fishes_new[(fishRouteCheckResult[0],fishRouteCheckResult[1])] = [fishRouteCheckResult[2]]
                else:
                    fishList.append(fish_d)
                    fishes_new[fish_geo]= fishList
            if (len(fishList)>0):
                fishes_new[fish_geo] = fishList 
        fishes = fishes_new
        # print("이동 후 ")
        # 상어 이동
        shark_map, fishes, new_shark_geo = move_shark(fishes, shark_map, S_y, S_x)
        S_y = new_shark_geo[0]
        S_x = new_shark_geo[1]
        # print("삭제 후 ")
        # 상어의 복사 마법 실행!
        for fishGeo in duplicate_magic.keys():
            if fishGeo in fishes:
                tmpList = fishes[fishGeo]
                appendList = duplicate_magic[fishGeo]
                for i in appendList:
                    tmpList.append(i)
                fishes[fishGeo] = tmpList
            else:
                appendList = duplicate_magic[fishGeo]
                fishes[fishGeo] = appendList
        for i in range(5):
            for j in range(5):
                shark_map[i][j] = shark_map[i][j]-1
        # print("복사 후 ")
    ans = 0
    for key in fishes.keys():
        ans += len(fishes[key])
    return ans

if __name__ == '__main__':
    # nPr = product(d_xy_shark, repeat = 3)
    M, S = map(int, input().split(' '))
    fishes = dict()
    shark_map = [[0 for i in range(5)] for j in range(5)]
    for i in range(M):
        f_y,f_x,d = map(int, sys.stdin.readline().split(' '))
        if (f_y, f_x) in fishes:
            fishList = fishes[(f_y,f_x)]
            fishList.append(d)
            fishes[(f_y,f_x)] = fishList
        else:
            fishes[(f_y,f_x)] = [d]
            
    S_y, S_x = map(int, input().split(' '))

    print(show_magic(shark_map, fishes, S_y, S_x, S, M))

    
