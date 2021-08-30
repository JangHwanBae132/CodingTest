import heapq
from collections import deque

def solution(jobs):
    jobs.sort(key= lambda x: x[1])
    jobs.sort(key= lambda x: x[0])

    queue= deque(jobs)
    heap =[]
    init = queue.popleft()
    answer = init[1]
    currentTime = init[1]+init[0]
    while True:
        if len(heap) ==0 and len(queue)==0:
            return answer // len(jobs)

        while True:
            if len(queue) != 0 and queue[0][0] <= currentTime:
                que_pop = queue.popleft()
                answer += -que_pop[0]
                heapq.heappush(heap, que_pop[1])
            else:
                break

        if len(heap) != 0:
            heap_pop = heapq.heappop(heap)
            currentTime+=heap_pop
            answer += currentTime
        elif len(queue)!=0 and queue[0][0] > currentTime:
            que_pop = queue.popleft()
            answer += que_pop[1]
            currentTime += que_pop[0]+que_pop[1]-currentTime

    return answer

