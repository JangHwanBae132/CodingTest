# 답은 되지만 상당히 비효율적인 코드인 효율성 평가를 안하는 코딩테스트 문제이니 그냥 함

def solution(N, number):
    answer = 0
    # key가 N인 dic
    NDic = {1: [N], 2: [N * 11], 3: [N * 111], 4: [N * 1111], 5: [N * 11111], 6: [N * 111111], 7: [N * 1111111],
            8: [N * 11111111]}
    # key가 number Dic, value: N
    NumDic = {N: 1, N * 11: 2, N * 111: 3, N * 1111: 4, N * 11111: 5}

    for i in range(2, 9):
        for j in range(1, i):
            for a in NDic[j]:
                for b in NDic[i - j]:
                    if (a + b) not in NDic[i]:
                        NDic[i].append(a + b)
                    if a + b not in NumDic.keys():
                        NumDic[a + b] = i
                    if a - b not in NDic[i]:
                        NDic[i].append(a - b)
                    if a - b not in NumDic.keys():
                        NumDic[a - b] = i
                    if a * b not in NDic[i]:
                        NDic[i].append(a * b)
                    if a * b not in NumDic.keys():
                        NumDic[a * b] = i
                    if b != 0:
                        if int(a / b) not in NDic[i]:
                            NDic[i].append(int(a / b))
                        if int(a / b) not in NumDic.keys():
                            NumDic[int(a / b)] = i

    if number in NumDic.keys():
        return NumDic[number]
    else:
        return -1
