import copy
import math
def dfs(nowIndex, emoticons, newEmoticons, discountRate, users, imoticonCnt):
    
    if(nowIndex < imoticonCnt):
        resultList = []

        for rate in discountRate:
            # print("nowIndex : ", nowIndex, "\nrate : ", rate)
            nowEmoticon = emoticons[nowIndex]
            newBillOfEmoticon = nowEmoticon*(1-rate)
            test = (rate*100, newBillOfEmoticon)
            tmpNewEmoticon = list()
            tmpNewEmoticon = copy.deepcopy(newEmoticons)
            tmpNewEmoticon.append(test)
            resultList.append(dfs(nowIndex+1, emoticons, tmpNewEmoticon, discountRate, users, imoticonCnt))
        resultList.sort(reverse=True)
        return resultList[0]
    else:
        # print(nowIndex, emoticons, newEmoticons, discountRate, users, imoticonCnt)
        emoticonPlusCnt = 0
        emoticonSold = 0
        # print("users: ", users, "\nnowEmoticons : ", newEmoticons)
        for user in users:
            userMoney = 0
            for emoticon in newEmoticons:
                if user[0] <= emoticon[0]:
                    userMoney += emoticon[1]
            if userMoney >= user[1]:
                emoticonPlusCnt += 1
            else:
                emoticonSold += userMoney
        result = (emoticonPlusCnt, math.floor(emoticonSold))
        return result
        # print(result)

def solution(users, emoticons):
    discountRate = [0.1,0.2,0.3,0.4]
    result = dfs(0, emoticons, list(), discountRate, users, len(emoticons))

    return list(result)

if __name__ == '__main__':
    users = [[40, 2900], [23, 10000], [11, 5200], [5, 5900], [40, 3100], [27, 9200], [32, 6900]]
    emoticons =  [1300, 1500, 1600, 4900]
    print(solution(users,emoticons))