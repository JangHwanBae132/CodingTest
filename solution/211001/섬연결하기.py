import heapq
import math
from collections import defaultdict, deque


def solution(n, costs):
    graph = defaultdict(list)
    costs.sort(key= lambda x : x[2])
    cost_array = [math.inf for i in range(n)]
    visited = [[1 if i == j else 0 for i in range(n)] for j in range(n)]

    for cost in costs:
        graph[cost[0]].append((cost[1],cost[2]))
        graph[cost[1]].append((cost[0],cost[2]))

    queue= []
    heapq.heappush(queue, (0,0))
    cost_array[0] = 0

    while queue:
        cost, current_node = heapq.heappop(queue)
        if cost_array[current_node] < cost:
            continue

        for next_node, add_cost in graph[current_node]:
            if cost_array[next_node] > add_cost and visited[current_node][next_node] == 0:
                cost_array[next_node]= add_cost
                heapq.heappush(queue, (add_cost, next_node))
                visited[current_node][next_node] = 1
                visited[next_node][current_node] = 1

    return sum(cost_array)
