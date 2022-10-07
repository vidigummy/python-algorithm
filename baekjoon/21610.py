"""
문제
마법사 상어는 파이어볼, 토네이도, 파이어스톰, 물복사버그 마법을 할 수 있다. 오늘 새로 배운 마법은 비바라기이다. 비바라기를 시전하면 하늘에 비구름을 만들 수 있다. 오늘은 비바라기를 크기가 N×N인 격자에서 연습하려고 한다. 격자의 각 칸에는 바구니가 하나 있고, 바구니는 칸 전체를 차지한다. 바구니에 저장할 수 있는 물의 양에는 제한이 없다. (r, c)는 격자의 r행 c열에 있는 바구니를 의미하고, A[r][c]는 (r, c)에 있는 바구니에 저장되어 있는 물의 양을 의미한다.

격자의 가장 왼쪽 윗 칸은 (1, 1)이고, 가장 오른쪽 아랫 칸은 (N, N)이다. 마법사 상어는 연습을 위해 1번 행과 N번 행을 연결했고, 1번 열과 N번 열도 연결했다. 즉, N번 행의 아래에는 1번 행이, 1번 행의 위에는 N번 행이 있고, 1번 열의 왼쪽에는 N번 열이, N번 열의 오른쪽에는 1번 열이 있다.

비바라기를 시전하면 (N, 1), (N, 2), (N-1, 1), (N-1, 2)에 비구름이 생긴다. 구름은 칸 전체를 차지한다. 이제 구름에 이동을 M번 명령하려고 한다. i번째 이동 명령은 방향 di과 거리 si로 이루어져 있다. 방향은 총 8개의 방향이 있으며, 8개의 정수로 표현한다. 1부터 순서대로 ←, ↖, ↑, ↗, →, ↘, ↓, ↙ 이다. 이동을 명령하면 다음이 순서대로 진행된다.

모든 구름이 di 방향으로 si칸 이동한다.
각 구름에서 비가 내려 구름이 있는 칸의 바구니에 저장된 물의 양이 1 증가한다.
구름이 모두 사라진다.
2에서 물이 증가한 칸 (r, c)에 물복사버그 마법을 시전한다. 물복사버그 마법을 사용하면, 대각선 방향으로 거리가 1인 칸에 물이 있는 바구니의 수만큼 (r, c)에 있는 바구니의 물이 양이 증가한다.
이때는 이동과 다르게 경계를 넘어가는 칸은 대각선 방향으로 거리가 1인 칸이 아니다.
예를 들어, (N, 2)에서 인접한 대각선 칸은 (N-1, 1), (N-1, 3)이고, (N, N)에서 인접한 대각선 칸은 (N-1, N-1)뿐이다.
바구니에 저장된 물의 양이 2 이상인 모든 칸에 구름이 생기고, 물의 양이 2 줄어든다. 이때 구름이 생기는 칸은 3에서 구름이 사라진 칸이 아니어야 한다.
M번의 이동이 모두 끝난 후 바구니에 들어있는 물의 양의 합을 구해보자.

입력
첫째 줄에 N, M이 주어진다.

둘째 줄부터 N개의 줄에는 N개의 정수가 주어진다. r번째 행의 c번째 정수는 A[r][c]를 의미한다.

다음 M개의 줄에는 이동의 정보 di, si가 순서대로 한 줄에 하나씩 주어진다.

출력
첫째 줄에 M번의 이동이 모두 끝난 후 바구니에 들어있는 물의 양의 합을 출력한다.
"""
import sys


direction_list = [(0,-1),(-1,-1),(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1)]

def hi():
    print("hi")

def water_duplicate_magic(now_geo, graph_map, N):
    water_direction_list = [(-1,-1),(1,1),(-1,1),(1,-1)]
    cnt = 0
    for water_direction in water_direction_list:
        next_geo_y = now_geo[0]+water_direction[0]
        next_geo_x = now_geo[1]+water_direction[1]
        if(next_geo_y < 0 or next_geo_y >= N):
            continue
        if(next_geo_x < 0 or next_geo_x >= N):
            continue
        if(graph_map[next_geo_y][next_geo_x] > 0):
            cnt += 1
    return cnt
def solution(graph_map, d_s_list,cloud_dict, N, M):
    
    for step_number in range(M):
        # print("-------------",step_number,"-------------")
        # print("이번 이동은 : ",d_s_list[step_number])
        # print("구름 이동 전 : ",cloud_dict)
        # print("초기상태 버킷")
        # for row in graph_map:
        #     print(row)
        water_duplicate_magic_dict = dict()
        # 모든 구름이 d_i 방향으로 s_i칸 이동한다.
        now_direction = d_s_list[step_number][0]-1
        now_direction_cnt = d_s_list[step_number][1]
        new_cloud = dict()
        for cloud in cloud_dict.keys():
            new_y = cloud[0] + direction_list[now_direction][0]*now_direction_cnt
            new_x = cloud[1] + direction_list[now_direction][1]*now_direction_cnt
            new_cloud[(new_y%N, new_x%N)] = 1
        #  각 구름에서 비가 내려 구름이 있는 칸의 바구니에 저장된 물의 양이 1 증가한다.
        cloud_dict = new_cloud
        # print("구름 이동 후 : ",cloud_dict)
        for cloud in cloud_dict.keys():
            # 인덱스 에러 날까봐 처리
            if(cloud[0] < 0 or cloud[0] >= N):
                continue
            if(cloud[1] < 0 or cloud[1] >= N):
                continue
            graph_map[cloud[0]][cloud[1]] += 1
        # 구름이 모두 사라진다.
            water_duplicate_magic_dict[(cloud[0],cloud[1])] = 1
        new_cloud = dict()
        # 2에서 물이 증가한 칸 (r, c)에 물복사버그 마법을 시전한다. 물복사버그 마법을 사용하면, 대각선 방향으로 거리가 1인 칸에 물이 있는 바구니의 수만큼 (r, c)에 있는 바구니의 물이 양이 증가한다.
        for water_duplicate_magic_place in water_duplicate_magic_dict.keys():
            result = water_duplicate_magic(water_duplicate_magic_place, graph_map, N)
            graph_map[water_duplicate_magic_place[0]][water_duplicate_magic_place[1]] += result
        # print("물복사 마법 후 : ")
        # for row in graph_map:
        #     print(row)
        # 바구니에 저장된 물의 양이 2 이상인 모든 칸에 구름이 생기고, 물의 양이 2 줄어든다. 이때 구름이 생기는 칸은 3에서 구름이 사라진 칸이 아니어야 한다.
        for y in range(N):
            for x in range(N):
                if graph_map[y][x] >= 2 and (y,x) not in cloud_dict:
                    new_cloud[(y,x)] = 1
                    graph_map[y][x] -= 2
        cloud_dict = new_cloud
        # print("비바라기 이후 구름 : ",cloud_dict)
        # print("비바라기 이후 버킷 : ",graph_map)
    result = 0
    for row in graph_map:
        result += sum(row)
    return result
        
if __name__ == "__main__":
    N, M = map(int, sys.stdin.readline().split(' '))
    input_graph = [0 for i in range(N)]
    bucket_list = [0 for i in range(N)]
    for i in range(N):
        line = [*map(int, sys.stdin.readline().split(' '))]
        input_graph[i] = line
            
    cloud_dict = dict()
    cloud_dict[(N-1,0)] = 1
    cloud_dict[(N-1,1)] = 1
    cloud_dict[(N-2,0)] = 1
    cloud_dict[(N-2,1)] = 1 
    d_s_list = [0 for i in range(M)]
    for i in range(M):
        d_i, s_i = map(int, input().split(' '))
        d_s_list[i] = (d_i,s_i)

    print(solution(input_graph,d_s_list,cloud_dict,N,M))