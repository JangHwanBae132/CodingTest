from collections import deque


def solution(priorities, location):
    answer = 0
    dic = {}
    que = deque()
    for i in range(len(priorities)):
        que.append([priorities[i],i])

    for p in priorities:
        if p not in dic.keys():
            dic[p] = 1
        else:
            dic[p]=dic[p]+1

    prior = []
    for p in dic:
        prior.append([ p, dic[p]])

    prior.sort(key= lambda x: x[0], reverse=True)

    cnt =0
    while(que):
        pop = que.popleft()
        if pop[0] == prior[0][0]:
            cnt += 1
            if pop[1] == location:
                print(cnt)
                return cnt

            if prior[0][1] == 1:
                prior.pop(0)
            else:
                prior[0][1] += -1
        else:
            que.append(pop)

    return answer
