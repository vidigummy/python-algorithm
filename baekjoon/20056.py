import sys
from collections import deque
direction_list = [(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1)]
new_direction_list_list = [(0,2,4,6),(1,3,5,7)]
def make_new_geo(now_geo, direction, speed, N):
    y = now_geo[0]
    x = now_geo[1]
    direction_y = direction_list[direction][0]
    direction_x = direction_list[direction][1]
    for i in range(speed):
        y += direction_y
        x += direction_x
        if(y < 1):
            y = N
        elif(y > N):
            y = 1
        if(x < 1):
            x = N
        elif(x > N):
            x = 1
    return (y,x)
    

def make_new_fireballs(now_fireballs):
    cnt_fireball = len(now_fireballs)
    even_odd = 0
    weight = 0
    speed = 0
    while now_fireballs:
        fireball = now_fireballs.popleft()
        if(fireball[2]%2 == 0):
            even_odd += 1
        else:
            even_odd -= 1
        weight += fireball[0]
        speed += fireball[1]
    if(abs(even_odd) == cnt_fireball):
        new_deque = deque()
        new_direction_list = new_direction_list_list[0]
        new_m = weight//5
        
        if new_m > 0:
            new_s = speed//cnt_fireball
            for i in new_direction_list:
                new_deque.append((new_m,new_s,i))
        return new_deque
        
    else:
        new_deque = deque()
        new_direction_list = new_direction_list_list[1]
        new_m = weight//5
        if new_m > 0:
            new_s = speed//cnt_fireball
            for i in new_direction_list:
                new_deque.append((new_m,new_s,i))
        return new_deque

def solution(fireballs_geo_map, N, K):
    
    for magic_step in range(K):
        # 이동하자 구구구
        # print("------------------",magic_step,"------------------")
        # print("이동 전 : ",fireballs_geo_map)
        new_fireballs_geo_map = dict()
        for geo in fireballs_geo_map.keys():
            fireball_list =fireballs_geo_map[geo]
            for fireball in fireball_list:
                new_geo = make_new_geo(geo,fireball[2],fireball[1],N)
                if new_geo in new_fireballs_geo_map:
                    tmp_deque = new_fireballs_geo_map[new_geo]
                    tmp_deque.append(fireball)
                    new_fireballs_geo_map[new_geo] = tmp_deque
                else:
                    tmp_deque = deque()
                    tmp_deque.append(fireball)
                    new_fireballs_geo_map[new_geo] = tmp_deque
        fireballs_geo_map = new_fireballs_geo_map
        # print("이동 후",fireballs_geo_map)
        # 두개 이상의 파이어볼이 있는 곳을 찾자.
        new_fireballs_geo_map = dict()
        for geo in fireballs_geo_map.keys():
            if(len(fireballs_geo_map[geo])> 1):
                # 같은 칸에 있는 파이어볼은 하나로 합쳐진다.
                new_fireballs = make_new_fireballs(fireballs_geo_map[geo])
                if(len(new_fireballs) > 1):   
                    new_fireballs_geo_map[geo] = new_fireballs
            else:
                new_fireballs_geo_map[geo] = fireballs_geo_map[geo]
        fireballs_geo_map = new_fireballs_geo_map
    #     print("불덩이 후 : ",fireballs_geo_map)
    # print("종료 후 : ",fireballs_geo_map)
    result = 0
    for geo in fireballs_geo_map.keys():
        fireball_list = fireballs_geo_map[geo]
        for fireball in fireball_list:
            result += fireball[0]
    return result
if __name__ == '__main__':
    N, M, K = map(int, sys.stdin.readline().split(' '))
    fireballs = dict()
    fireballs_geo_map = dict()
    for i in range(M):
        input_line = [*map(int, sys.stdin.readline().split(' '))]
        y,x = input_line[0],input_line[1]
        m = input_line[2]
        d = input_line[4]
        s = input_line[3]
        tmp_deque = deque()
        tmp_deque.append((m,s,d))
        fireballs_geo_map[(y,x)] = tmp_deque
    print(solution(fireballs_geo_map,N,K))
        