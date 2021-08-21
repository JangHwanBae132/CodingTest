import sys
read = sys.stdin.readline
from collections import deque


def dfs(dic, V):
    visited = [V]
    stack = deque([V])
    while(stack):
        top = stack[-1]
        if top not in dic:
            break
        if len(dic[top]) != 0:
            if dic[top][0] in visited:
                dic[top] = dic[top][1:]
            else:
                stack.append(dic[top][0])
                visited.append(dic[top][0])
                dic[top] = dic[top][1:]
        else:
            stack.pop()
    df = ""
    for a in visited:
        df= df + " "+str(a)
    print(df.strip())

def bfs(dic, V):
    visited = [V]
    queue = deque([V])

    while(queue):
        top = queue.popleft()
        print(top, end = " ")
        if top not in dic:
            break
        for a in dic[top]:
            if a not in visited:
                visited.append(a)
                queue.append(a)

N,M,V = map(int,read().split())

dic = {}
for i in range(M):
    a,b = map(int,read().split())
    if a in dic.keys():
        dic[a].add(b)
    else:
        dic[a] = set()
        dic[a].add(b)
    if b in dic.keys():
        dic.get(b).add(a)
    else:
        dic[b] = set()
        dic[b].add(a)

for a in dic.keys():
    l = list(dic[a])
    dic[a] = l

for a in dic.keys():
    dic[a].sort()

dfs(dic.copy(), V)
bfs(dic.copy(), V)
