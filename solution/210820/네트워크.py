from collections import deque

def solution(n, computers):
    answer = 0
    hashset= set()

    for i in range(n):
        if i not in hashset:
            answer+=1
            hashset = bfs(i, n , computers, hashset)

    print(answer)
    return answer

def bfs(i, n ,computers, hashset):
    que = deque()
    for j in range(n):
        if i !=j and computers[i][j] == 1 and j not in hashset:
            que.append(j)
            hashset.add(j)
    while que:
        hashset = bfs(que.popleft(), n, computers, hashset)

    return hashset
