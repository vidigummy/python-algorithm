from typing import List
from itertools import product
def checkCanChange(now, targetList, dotList, canChange, k):
    canChangeLen = (len(now), len(now)-len(dotList)+len(dotList)*k)
    cnt = 0
    for target in targetList:
        if(len(target)>= canChangeLen[0] and len(target)<= canChangeLen[1]):
            cnt += 1
    if cnt <= 0:
        return False

    cnt =0 
    exceptDotList = now.split('.')
    if len(exceptDotList) > 0:
        for exceptDot in exceptDotList:
            for target in targetList:
                if(exceptDot in target):
                    cnt += 1
        if cnt <= 0:
            return False

    canChangeList = product(canChange, repeat=len(dotList))
    for i in canChangeList:
        canChangeWord = list(now)
        for j in range(len(dotList)):
            canChangeWord[dotList[j]] = i[j]
        changedWord = ''.join(canChangeWord)
        if changedWord in targetList:
            return True
    return False

def solution(k: int, dic: List[str], chat: str) -> str:
    alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    
    canChange = []
    for i in range(1, k+1):
        nPr = product(alphabet, repeat=i)
        for j in nPr:
            canChange.append(''.join(j))

    chatSlice = chat.split(' ')
    for i in range(len(chatSlice)):
        #첫번째 필터링
        for word in dic:
            if word == chatSlice[i]:
                chatSlice[i] = ''.join(['#' for i in range(len(word))])
        # 두번째 필터링
        if '.' in chatSlice[i]:
            startCnt = chatSlice[i].count('.')
            whereStarts = list(filter(lambda x: chatSlice[i][x] == '.', range(len(chatSlice[i]))))
            if(checkCanChange(chatSlice[i],dic,whereStarts,canChange,k) == True):
                chatSlice[i] = ''.join(['#' for j in range(len(chatSlice[i]))])
            
    return ' '.join(chatSlice)




if __name__ == '__main__':
    k = 3
    dic = ["abcde", "cdefg", "efgij"]
    chat = ".. ab. cdefgh .gi. .z."
    print(solution(k, dic, chat))