import sys
read = sys.stdin.readline
from collections import deque


def adjacent(_status,_position):
    adj = []
    if _position[0] != 0 and _status == field[_position[0]-1][_position[1]]:
        adj.append([_position[0]-1, _position[1]])
    if _position[0] != M-1 and _status == field[_position[0]+1][_position[1]]:
        adj.append([_position[0]+1, _position[1]])
    if _position[1] != 0 and _status == field[_position[0]][_position[1]-1]:
        adj.append([_position[0], _position[1]-1])
    if _position[1] != N-1 and _status == field[_position[0]][_position[1]+1]:
        adj.append([_position[0], _position[1]+1])
    return adj

N, M = map(int, read().split())
field = [list(read().strip()) for _ in range(M)]
visited= [[0 for col in range(N)] for row in range(M)]
queue = deque()
W_C = []
B_C = []
cnt = 0;
status = "";
for i in range(M):
    for j in range(N):
        if visited[i][j] == 0:
            queue.append([i,j])
            status = field[i][j]
        while(queue):
            pop = queue.popleft()
            if visited[pop[0]][pop[1]] == 0:
                visited[pop[0]][pop[1]] = 1
                cnt =cnt+ 1
                adj = adjacent(field[pop[0]][pop[1]], pop)
                for a in adj:
                    queue.append(a)
            # print(cnt)
        if status == "W":
            W_C.append(cnt)
        elif status == "B":
            B_C.append(cnt)

        status = ""
        cnt = 0

w = 0
for _w in W_C:
    w += _w*_w

b = 0
for _b in B_C:
    b += _b*_b

print(str(w)+ " "+str(b))

