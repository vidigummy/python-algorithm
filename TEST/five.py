from tkinter.tix import MAX
from typing import List
import math

def checkRight(a,b, feeList):
    for i in range(len(feeList)):
        if ((math.floor(feeList[i][0]/a)+1) * b != feeList[i][1]):
            return False
    return True
def solution(fees: List[List[int]], t: int) -> List[int]:
    answer =[2147483647,-2147483648]
    fees.sort()
    cnt = 0
    for a in range(1, 100):
        for b in range(1, fees[0][1]+1):
            # print(a,b)
            if(checkRight(a,b,fees)):
                # print("hihi")
                cnt += 1
                test = (math.floor(t/a)+1)*b
                if(test < answer[0]):
                    answer[0] = test
                if(test > answer[1]):
                    answer[1] = test
                # print(answer)
    if cnt == 0:
        return [-1]
    return answer

if __name__ == "__main__":
    fees = [[4, 1000], [6, 1000], [21, 3000], [16, 2000], [26, 3000]]
    t = 27
    print(solution(fees, t))