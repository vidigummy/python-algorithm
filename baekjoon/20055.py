import sys
from collections import deque


def solution(belt, N, K):
    cnt = 0
    step = 0
    robot_with_index = dict()
    while True:
        step += 1
        # print("--------------------step : ",step,"--------------------")
        # print("회전 전 belt : ",belt)
        # print("회전 전 로봇 : ", robot_with_index)
        new_belt = dict()
        new_robot_with_index = dict()
        # 벨트 및 로봇 회전
        for belt_i in belt.keys():
            new_belt[(belt_i+1)%(2*N)] = belt[belt_i]
        for robot_index in robot_with_index:
            new_robot_with_index[(robot_index+1)%(2*N)] = 1
        belt = new_belt
        robot_with_index = new_robot_with_index
        # 로봇이 N에 있는지 확인 후 삭제
        if(N-1 in robot_with_index):
            del(robot_with_index[N-1])
        
        # print("회전 후 belt : ",belt)
        # print("회전 후 로봇 : ", robot_with_index)
        # 로봇 이동
        for robot_index in sorted(robot_with_index.keys(), reverse=True):
            next_robot_index = (robot_index+1)%(2*N)
            # 이동할 벨트의 내구성이 없거나, 새로운 위치에 로봇이 있다면 이동 안 함.
            if belt[next_robot_index] != 0 and next_robot_index not in robot_with_index:
                belt[next_robot_index] = belt[next_robot_index]-1
                # print("next_robot_index : ",next_robot_index)
                # print("belt[next_robot_index] : ",belt[next_robot_index])
                if(belt[next_robot_index] == 0):
                    cnt += 1
                    # print("cnt : ",cnt)
                robot_with_index[next_robot_index] = 1
                del(robot_with_index[robot_index])
            # else:
            #     print("can't Go!")
        # 로봇이 N에 있는지 확인 후 삭제
        if(N-1 in robot_with_index):
            del(robot_with_index[N-1])
        # print("이동 후 belt : ",belt)
        # print("이동 후 로봇 : ", robot_with_index)
        # 올리는 위치 확인, 로봇 올려놓기
        if belt[0] > 0:
            robot_with_index[0] = 1
            belt[0] = belt[0]-1
            if(belt[0] < 1):
                cnt += 1
        # 내구도가 0인 칸의 개수가 K개 이상이라면 break
        if cnt >= K:
            break
    return step

if __name__ == "__main__":
    N, K = map(int, sys.stdin.readline().split(' '))
    belt = dict()
    line = [*map(int, sys.stdin.readline().split(' '))]
    for i in range(len(line)):
        belt[i] = line[i]
    
    print(solution(belt,N,K))