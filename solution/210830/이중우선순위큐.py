import heapq

def solution(operations):
    answer = []
    total = 0
    min_heap =[]
    max_heap =[]

    for o in operations:
        # 파이썬 조건문 확인 잘하자
        if o[0:2] == "I ":
            heapq.heappush(min_heap, int(o[2:]))
            heapq.heappush(max_heap, -int(o[2:]))
            total += 1
        elif total != 0 and o[0:3]=="D 1":
            heapq.heappop(max_heap)
            total += -1
        elif total !=0 and o[0:4] =="D -1":
            heapq.heappop(min_heap)
            total += -1

        if total == 0:
            min_heap = []
            max_heap = []

    if total == 0:
        return [0,0]
    else:
        return [-heapq.heappop(max_heap), heapq.heappop(min_heap)]
