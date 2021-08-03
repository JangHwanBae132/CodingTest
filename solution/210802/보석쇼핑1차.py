from collections import deque

def solution(gems):
    answer = []
    hashSet = set(gems)
    start =1;
    end=0;
    que = deque()
    short_sector = 100000
    isAll = False
    for g in gems:
        que.append(g)
        end += 1

        if isAll is False:
            if len(set(que))==len(hashSet):
                isAll = True

        while(isAll):
            if que.count(que[0]) >1:
                que.popleft()
                start += 1
            else:
                break;


        if isAll and end-start < short_sector:
            short_sector = end -start
            answer =[start, end]

    return answer
