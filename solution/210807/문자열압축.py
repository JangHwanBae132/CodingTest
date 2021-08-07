import math

def solution(s):
    answer = len(s);

    for i in range(1,int(len(s)/2)+1):
        sSplit = []
        for j in range(math.ceil(len(s)/i)):
            sSplit.append(s[j*i:(j+1)*i])

        # print(sSplit)
        tempCnt = 1;
        tempAns = i;

        for j in range(len(sSplit)-1):
            # print(tempAns)
            if sSplit[j] == sSplit[j+1]:
                tempCnt += 1
                if j+1 == len(sSplit)-1:
                    tempAns+=len(str(tempCnt))
                    tempCnt = 1
            else:
                if tempCnt != 1:
                    tempAns+=len(str(tempCnt))
                tempAns += len(sSplit[j+1])
                tempCnt =1

        # print(tempAns)
        if tempAns < answer:
            answer = tempAns
        tempAns = 0;


    print(answer)
    return answer



sArr = ["aabbaccc", "ababcdcdababcdcd", "abcabcdede", "abcabcabcabcdededededede" ,"xababcdcdababcdcd", "aaaaaaaaaa"]

# solution(sArr[1])

for s in sArr:
    solution(s)
