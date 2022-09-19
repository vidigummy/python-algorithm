
import itertools

def solution(k, dungeons):
    answer = -1
    nPr = itertools.permutations(dungeons)
    for i in nPr:
        nowK = k
        cnt = 0
        for j in i:
            if nowK >= j[0]:
                cnt+=1
                nowK -= j[1]
            else:
                break
        if cnt > answer:
            answer = cnt
    return answer


if __name__ == '__main__':
    k = 80
    dungeons = [[80,20],[50,40],[30,10]]
    print(solution(k,dungeons))