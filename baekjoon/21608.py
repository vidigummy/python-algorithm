import sys
from collections import deque
import math
direction_list = [(-1,0),(1,0),(0,-1),(0,1)]

def cnt_like_student(y,x,student_map, student_like_list_dict, now_student, N):
    cnt = 0
    for direction in direction_list:
        next_y = y+direction[0]
        next_x = x+direction[1]
        if not next_y < 0 and not next_x < 0 and not next_y >= N and not next_x >= N:
            if(student_map[next_y][next_x] in student_like_list_dict[now_student]):
                cnt += 1
    return cnt

def find_great_place(N, student_map, student_like_list_dict, now_student, student_spare_map):
    max = -100
    max_dict = dict()
    for y in range(N):
        for x in range(N):
            if student_map[y][x] < 0:
                # 좋아하는 학생이 많이 앉은 cnt
                cnt = cnt_like_student(y,x, student_map, student_like_list_dict, now_student, N)
                # print("y,x,cnt : ", (y,x,cnt))
                if cnt > max:
                    max_dict.clear()
                    max = cnt
                    max_dict[(y,x)] = student_spare_map[(y,x)]
                elif cnt == max:
                    max_dict[(y,x)] = student_spare_map[(y,x)]
    # 여기선 좋아하는 학생이 주변에 가장 많이 앉은 자리만 존재함.
    # 그렇다면, 비어있는칸(spare_map) 기준, 그 다음은, 행-열 기준이다.
    sorted_max_dict = sorted(max_dict.items(), key = lambda x : (-x[1], x[0][0], x[0][1]))
    # print(sorted_max_dict)
    return sorted_max_dict[0][0]

def make_student_spare_map_dict(N):
    student_spare_map = dict()
    for y in range(N):
        for x in range(N):
            cnt = 0
            for direction in direction_list:
                next_y = y+direction[0]
                next_x = x+direction[1]
                if not next_y < 0 and not next_x < 0 and not next_y >= N and not next_x >= N:
                    cnt += 1
                student_spare_map[(y,x)] = cnt
    return student_spare_map
            
def solution(student_like_list_dict, N, student_list):
    ans = 0
    student_spare_map_dict = make_student_spare_map_dict(N)
    # print(student_spare_map_dict)
    student_map = [[-1 for i in range(N)] for j in range(N)]
    while student_list:
        now_student = student_list.popleft()
        # print("----------------------------")
        # print(now_student)
        # 최적의 자리 찾기
        result = find_great_place(N, student_map, student_like_list_dict, now_student, student_spare_map_dict)
        # print(result)
        # 최적의 자리를 찾았으면, 자리에 표시를 해준다.
        student_map[result[0]][result[1]] = now_student
        # 주변 자리에 주변에 빈 자리가 하나 줄었다고 알려줌.
        for direction in direction_list:
            del_y = result[0]+direction[0]
            del_x = result[1]+direction[1]
            if (del_y,del_x) in student_spare_map_dict:
                student_spare_map_dict[(del_y,del_x)] -= 1
        # 만족도 조사.
    for y in range(N):
        for x in range(N):
            cnt = cnt_like_student(y,x, student_map, student_like_list_dict, student_map[y][x], N)
            if(cnt > 0):
                point = math.floor(math.pow(10,cnt-1))
                # print(point)
                ans += point
    # print(ans)
    return ans

        
if __name__ == "__main__":
    N = [*map(int, sys.stdin.readline().split(' '))][0]
    student_like_list_dict = dict()
    student_list = deque()
    for i in range(N*N):
        temp_dict = dict()
        line = [*map(int, sys.stdin.readline().split(' '))]
        student = line[0]
        student_like_list = line[1:]
        for like_student in student_like_list:
            temp_dict[like_student] = True
        student_list.append(student)
        student_like_list_dict[student] = temp_dict
    result = solution(student_like_list_dict, N, student_list)
    print(result)