
from typing import List

def newArray(new):
    ans = 1
    while ans < new:
        ans *= 2
    return ans

def solution(queries: List[List[int]]) -> int:
    answer = -1
    nowSangTae = dict()
    for querie in queries:
        if querie[0] not in nowSangTae:
            newLen = newArray(querie[1])
            newTuple = (querie[1], newLen)
            nowSangTae[querie[0]] = newTuple
        else:
            nowTuple = nowSangTae[querie[0]]
            # print(nowTuple)
            newMaxLen = nowTuple[1]
            if nowTuple[0]+querie[1] > nowTuple[1]:
                newMaxLen = newArray(nowTuple[0]+querie[1])
                answer += nowTuple[0]
            nowSangTae[querie[0]] = (nowTuple[0]+querie[1], newMaxLen)
        # print(answer)
    return answer+1

if __name__ == '__main__':
    queries = [[2,10],[7,1],[2,5],[2,9],[7,32]]
    print(solution(queries))