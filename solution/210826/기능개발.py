from collections import deque

def solution(progresses, speeds):
    answer = []
    s= 0
    cnt =1
    temp =0
    queue = deque(progresses)

    while(queue):
        if queue[0]+cnt*speeds[s] >= 100:
            s += 1
            queue.popleft()
            temp +=1
        elif temp != 0:
            cnt += 1
            answer.append(temp)
            temp = 0
        else:
            cnt += 1
            temp = 0
    answer.append(temp)
    return answer
