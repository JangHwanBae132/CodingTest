import heapq

def solution(scoville, K):
    answer=0
    _K = False
    heap = []
    for s in scoville:
        if s < K:
            heapq.heappush(heap,s)
        else:
            _K = True

    while True:
        if len(heap) <2:
            if _K:
                return answer+1
            else:
                return -1
        h1 = heapq.heappop(heap)
        h2 = heapq.heappop(heap)
        new_h = h1+h2*2
        answer+=1
        if new_h < K:
            heapq.heappush(heap,new_h)
        elif len(heap)==0:
            return answer
        elif len(heap)==1:
            return answer+1
    return -1
