import sys
# 0은 동, 1은 서, 2는 남, 3은 북
dice_x_y = [(0,1),(0,-1),(1,0),(-1,0)]
dice_map = [
        [2],
    [4],[1],[3],
        [5],
        [6]
]

def new_dice_map( next_direction):
    global dice_map
    if(next_direction == 2):
        tmp = dice_map[0]
        dice_map[0] = dice_map[2]
        dice_map[2] = dice_map[4]
        dice_map[4] = dice_map[5]
        dice_map[5] = tmp
    elif(next_direction == 3):
        tmp = dice_map[5]
        dice_map[5] = dice_map[4]
        dice_map[4] = dice_map[2]
        dice_map[2] = dice_map[0]
        dice_map[0] = tmp
    elif(next_direction == 0):
        new_dice = [0 for i in range(6)]
        new_dice[2] = dice_map[1] #나 자신
        new_dice[0] = dice_map[0] #북쪽
        new_dice[1] = dice_map[5] #서쪽 
        new_dice[3] = dice_map[2] #동쪽
        new_dice[4] = dice_map[4] #남쪽
        new_dice[5] = dice_map[3] #7-자신
        dice_map = new_dice
    else:
        new_dice = [0 for i in range(6)]
        new_dice[2] = dice_map[3] #나 자신
        new_dice[0] = dice_map[0] #북쪽
        new_dice[1] = dice_map[2] #서쪽 
        new_dice[3] = dice_map[5] #동쪽
        new_dice[4] = dice_map[4] #남쪽
        new_dice[5] = dice_map[1] #7-자신
        dice_map = new_dice
    return dice_map[2]
    
def dice_check_go(dice_geo,dice_direction, N, M):
    # print("***********dice_check_go********")
    # print("now : ",dice_geo)
    # print("now direction : ",dice_direction, " ", dice_x_y[dice_direction])
    dice_geo_x = dice_geo[1]
    dice_geo_y = dice_geo[0]
    next_dice_geo_x = dice_geo_x+dice_x_y[dice_direction][1]
    next_dice_geo_y = dice_geo_y+dice_x_y[dice_direction][0]
    if(next_dice_geo_x < 0):
        # 서쪽으로 간 경우
        return 0
    if(next_dice_geo_x >= M):
        # 동쪽으로 간 경우
        return 1
    if(next_dice_geo_y < 0):
        # 북쪽으로 간 경우
        return 2
    if(next_dice_geo_y >= N):
        # 남쪽으로 간 경우
        return 3
    return dice_direction

def check_go(now_y,now_x,N,M):
    can_go_direction = list()
    for i in range(4):
        can_y = now_y + dice_x_y[i][0]
        can_x = now_x + dice_x_y[i][1]
        if( can_x >= 0):
            if (can_x < M):
                if(can_y >= 0):
                    if(can_y < N):
                        can_go_direction.append(i)
    return can_go_direction

def bfs(now_y, now_x, graph, isVisit, B):
    

    isVisit[(now_y, now_x)] = True
    canGoList = list()
    can_go_direction = check_go(now_y,now_x, N,M)
    for direction in can_go_direction:
        next_y = now_y+dice_x_y[direction][0]
        next_x = now_x+dice_x_y[direction][1]
        if not (next_y, next_x) in isVisit:
            if graph[next_y][next_x] == B:
                canGoList.append((next_y,next_x))
    while len(canGoList) > 0:
        go = canGoList.pop(0)
        isVisit[go] = True
        
        can_go_direction = check_go(go[1],go[0], N,M)
        for direction in can_go_direction:
            next_y = go[0]+dice_x_y[direction][0]
            next_x = go[1]+dice_x_y[direction][1]
            if not (next_y, next_x) in isVisit:
                if(next_y < 0):
                    continue
                if(next_x < 0):
                    continue
                if(next_y >= N):
                    continue
                if(next_x >= M):
                    continue
                if graph[next_y][next_x] == B :
                    canGoList.append((next_y,next_x))
    C = len(isVisit.keys())
    # print("BFS 결과 : ",isVisit)    
    # print("C : ",C)
    # print("B : ",B)
    return C*B



    
def dice_move(N,M,K, graph, dice_geo, dice_direction, dice_upper):
    ans = 0
    for i in range(K):
        # 주사위 이동 방향 결정
        # print("======",i+1,"=====")
        # print("now : ", dice_geo)

        # print("주사위는 ",dice_x_y[dice_direction],"쪽으로 갈거야")
        # 주사위 이동 및 점수 획득
        dice_direction = dice_check_go(dice_geo, dice_direction, N, M)
        next_y = dice_geo[0]+dice_x_y[dice_direction][0]
        next_x = dice_geo[1]+dice_x_y[dice_direction][1]
        dice_geo = (next_y, next_x)
        dice_upper = new_dice_map(dice_direction)
        
        B = graph[next_y][next_x]
        newPoint = bfs(next_y, next_x,graph, dict(), B)
        # print("now Upper : ", dice_upper)
        # print("new geo : ", dice_geo)
        # print("new point : ", newPoint)
        ans += newPoint
        
        # print("지금 위치 ",dice_geo,", 지금 위에 있는 숫자 ",dice_upper,", B : ", B)
        # 다음 이동 방향 결정
        if((7-dice_upper[0]) < graph[next_y][next_x]):
            if(dice_direction == 0):
                dice_direction = 3
            elif(dice_direction == 1):
                dice_direction = 2
            elif(dice_direction == 2):
                dice_direction = 0
            else:
                dice_direction = 1
        elif((7-dice_upper[0]) > graph[next_y][next_x]):
            if(dice_direction == 0):
                dice_direction = 2
            elif(dice_direction == 1):
                dice_direction = 3
            elif(dice_direction == 2):
                dice_direction = 1
            else:
                dice_direction = 0
        global dice_map
    #     print("now dice_map : ",dice_map)
    #     print("new direction: ", dice_direction)
    # print("ans : ", ans)
    return ans


if __name__ == '__main__':
    N, M, K = map(int, sys.stdin.readline().split(' '))
    graph = [0 for i in range(N)]
    for i in range(N):
        graph[i] = [*map(int, sys.stdin.readline().split(' '))]
    dice_geo = (0,0)
    dice_direction = 0
    dice_upper = 1
    print(dice_move(N,M,K,graph,dice_geo, dice_direction, dice_upper))