from collections import deque


def solution(maps):
    answer =[]
    current = [0,0,1]
    n = len(maps)
    m = len(maps[0])
    queue = deque()
    queue.append(current)
    maps[0][0] = 0
    while queue:
        current = queue.popleft()
        if current[:2] == [n-1, m-1]:
            answer.append(current[2])

        if current[0] < n-1 and maps[current[0]+1][current[1]]==1:
            maps[current[0]+1][current[1]] = 0
            queue.append([current[0]+1, current[1], current[2]+1])

        if current[1] < m-1 and maps[current[0]][current[1]+1]==1:
            maps[current[0]][current[1]+1] = 0
            queue.append([current[0], current[1]+1, current[2]+1])

        if current[0] > 0 and maps[current[0]-1][current[1]]==1:
            maps[current[0]-1][current[1]] = 0
            queue.append([current[0]-1, current[1], current[2]+1])

        if current[1] > 0 and maps[current[0]][current[1]-1] == 1:
            maps[current[0]][current[1] - 1] = 0
            queue.append([current[0], current[1] - 1, current[2]+1])

    if len(answer) ==0:
        return -1
    else:
        return min(answer)
