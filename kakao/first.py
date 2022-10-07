from datetime import datetime, timedelta 
from dateutil.relativedelta import relativedelta
def solution(today, terms, privacies):
    answer = []
    termsDict = dict()
    for term in terms:
        termSplit = term.split(' ')
        termsDict[termSplit[0]] = termSplit[1]
    # print(termsDict)
    todayDate = datetime.strptime(today, "%Y.%m.%d")
    # print(todayDate)
    for i in range (len(privacies)):
        print(i)
        privacie = privacies[i]
        privacieSplit = privacie.split(' ')
        privacieDate = datetime.strptime(privacieSplit[0], "%Y.%m.%d")
        
        privacieTerm = int(termsDict[privacieSplit[1]])

        print(privacieTerm)
        privacieNowTerm = privacieDate+ relativedelta(months=privacieTerm, days=-1)
        print(privacieDate, privacieNowTerm, todayDate)
        if(todayDate>privacieNowTerm):
            answer.append(i+1)
    return answer


if __name__ == '__main__':
    today = "2020.01.01"
    terms = ["Z 3", "D 5"]
    privacies = ["2019.01.01 D", "2019.11.15 Z", "2019.08.02 D", "2019.07.01 D", "2018.12.28 Z"]
    print(solution(today, terms, privacies))