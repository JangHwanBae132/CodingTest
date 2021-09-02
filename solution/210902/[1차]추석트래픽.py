import heapq
from collections import deque


def solution(lines):
    answer = 0
    preprocess_lines = []
    for l in lines:
        split_l = l.split(" ")
        split_time = split_l[1].split(":")
        end = int((int(split_time[0]) * 60 * 60 + int(split_time[1]) * 60 + float(split_time[2]))*1000)
        during = int(float(split_l[2][:-1])*1000)
        start = end - during + 1
        preprocess_lines.append([start, end])

    check_point = set(sum(preprocess_lines, []))
    sorted_check_point = sorted(list(check_point))

    preprocess_lines.sort(key= lambda x : x[0])
    refer = preprocess_lines[0][0]
    for p in preprocess_lines:
        p[0] += -refer
        p[1] += -refer

    for i in range(len(sorted_check_point)):
        sorted_check_point[i] += -refer

    lines_que = deque(preprocess_lines)
    heap = []

    for cp in sorted_check_point:
        while True:
            if len(lines_que)!=0 and lines_que[0][0] <= cp+999:
                heapq.heappush(heap, lines_que.popleft()[1])
            else:
                break

        while True:
            if len(heap) != 0 and heap[0] < cp:
                heapq.heappop(heap)
            else:
                break

        if len(heap) > answer:
            answer = len(heap)


    return answer
