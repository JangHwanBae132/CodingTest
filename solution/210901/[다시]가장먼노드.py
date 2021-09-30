from collections import deque
import math


def solution(n, vertex):
    answer =0
    graph = dict()
    distances = [math.inf if i !=0 else 0 for i in range(n)]
    queue = deque()
    queue.append((0,0))

    for (i, j) in vertex:
        if i-1 in graph:
            graph[i-1].append(j-1)
        else:
            graph[i-1] = [j-1]

        if j-1 in graph:
            graph[j-1].append(i-1)
        else:
            graph[j-1] = [i-1]


    while queue:
        current_destination, current_distance = queue.popleft()

        if distances[current_destination] <current_distance:
            continue

        for new_destination in graph[current_destination]:
            distance = current_distance+1

            if distance < distances[new_destination]:
                distances[new_destination] = distance
                queue.append((new_destination, distance))

    long_distance = max(distances)

    for d in distances:
        if d == long_distance:
            answer +=1

    return answer
