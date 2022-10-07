from tkinter import E
import typing

def check(a):
    return isinstance(a, typing.List)

def solution(commands):
    answer = []
    table = dict()
    for i in range(1, 51):
        for j in range(1, 51):
            table[(i,j)] = 'EMPTY'
    for command in commands:
        commandSplit = command.split(' ')
        if(commandSplit[0] == 'MERGE'):
            # 내가 리스트일때(이미 병합되어있을 때)
            # print(type(table[(int(commandSplit[1]), int(commandSplit[2]))]))
            if(type(table[(int(commandSplit[1]), int(commandSplit[2]))]) == type([])):
                # 내가 가진 병합 리스트
                myTooGo = table[(int(commandSplit[1]), int(commandSplit[2]))][1:]
                # 내가 가진 병합 리스트의 값
                value = table[(int(commandSplit[1]), int(commandSplit[2]))][0]
                # 병합해야하는게 병합되어있다면
                if(type(table[(int(commandSplit[3]), int(commandSplit[4]))]) == type([])):
                    # 가야할 곳 확인
                    toCheckGo = table[(int(commandSplit[3]), int(commandSplit[4]))][1:]
                    # 가야할 곳 한번씩 돌면서
                    for toCheck in toCheckGo:
                        # 내가 가진 병합 리스트와 값 주입
                        tmp = table[toCheck]
                        tmp[0] = value
                        for myTo in myTooGo:
                            tmp.append(myTo)
                        table[toCheck] = tmp
                        # 내가 가진 병합 리스트에도 새로운 리스트 주입
                    for toGo in myTooGo:
                        tmp = table[toGo]
                        for check in toCheckGo:
                            tmp.append(check)
                        table[toGo] = tmp
                # 그냥 병합 안 되어 있는 것이라면
                else:
                    newList = table[(int(commandSplit[1]), int(commandSplit[2]))]
                    newList.append((int(commandSplit[3]), int(commandSplit[4])))
                    table[(int(commandSplit[3]), int(commandSplit[4]))] = newList
                    for togo in newList[1:]:
                        table[togo] = newList
            # 내가 리스트가 아닐때(병합되지 않았을 때)
            else:
                # 상대가 병합되어있을때
                if(type(table[(int(commandSplit[3]), int(commandSplit[4]))]) != type([])):
                    newList = list()
                    newList = [table[(int(commandSplit[1]), int(commandSplit[2]))],(int(commandSplit[1]), int(commandSplit[2])),(int(commandSplit[3]), int(commandSplit[4]))]
                    table[(int(commandSplit[1]), int(commandSplit[2]))]= newList
                    table[(int(commandSplit[3]), int(commandSplit[4]))]= newList
                #  상대가 병합되지 않았을 때
                else:
                    newList = table[(int(commandSplit[3]), int(commandSplit[4]))]
                    newList[0] = table[(int(commandSplit[1]), int(commandSplit[2]))]
                    newList.append((int(commandSplit[1]), int(commandSplit[2])))
                    table[(int(commandSplit[1]), int(commandSplit[2]))] = newList
                    for i in range(1, len(newList)-1):
                        table[i] = newList
        if(commandSplit[0] == 'UPDATE'):
            if(len(commandSplit) == 4):
                if(type(table[(int(commandSplit[1]), int(commandSplit[2]))]) == type([])):
                    toGo = table[(int(commandSplit[1]),int(commandSplit[2]))][1:]
                    for go in toGo:
                        table[go][0] = commandSplit[3]
                else:
                    table[(int(commandSplit[1]), int(commandSplit[2]))] = commandSplit[3]
            else:
                for key in table.keys():
                    item = table[key]
                    if(type(item) == type([])):
                        if(item[0] == commandSplit[1]):
                            item[0] = commandSplit[2]
                            table[key] = item
                    else:
                        if(table[key] == commandSplit[1]):
                            table[key] = commandSplit[2]


        if(commandSplit[0] == 'UNMERGE'):
            tableList = table[(int(commandSplit[1]), int(commandSplit[2]))]
            value = tableList[0]
            for trash in tableList[1:]:
                table[trash] = 'EMPTY'
            table[(int(commandSplit[1]),int(commandSplit[2]))]= value
            print(table[(int(commandSplit[1]), int(commandSplit[2]))])

        if(commandSplit[0] == 'PRINT'):
            if(type(table[(int(commandSplit[1]), int(commandSplit[2]))]) == type([])):
                answer.append(table[(int(commandSplit[1]), int(commandSplit[2]))][0])
            else:
                answer.append(table[(int(commandSplit[1]), int(commandSplit[2]))])
        # print("---------------------------------------------------------\n",table,"\n---------------------------------------------------------")
    return answer

if __name__ == '__main__':
    # commands = ["UPDATE 1 1 menu", "PRINT 1 1"]
    commands = ["UPDATE 1 1 menu", "UPDATE 1 2 category", "UPDATE 2 1 bibimbap", "UPDATE 2 2 korean", "UPDATE 2 3 rice", "UPDATE 3 1 ramyeon", "UPDATE 3 2 korean", "UPDATE 3 3 noodle", "UPDATE 3 4 instant", "UPDATE 4 1 pasta", "UPDATE 4 2 italian", "UPDATE 4 3 noodle", "MERGE 1 2 1 3", "MERGE 1 3 1 4", "UPDATE korean hansik", "UPDATE 1 3 group", "UNMERGE 1 4", "PRINT 1 3", "PRINT 1 4"]
    print(solution(commands))