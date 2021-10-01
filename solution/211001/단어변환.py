from collections import deque, defaultdict


def can_change(begin, target):
    cnt = 0
    for i in range(len(begin)):
        if begin[i] != target[i]:
            cnt+=1
    if cnt == 1:
        return True
    else:
        return False

def make_graph(node, words, graph):
    for word in words:
        if can_change(node, word):
            graph[node].append(word)
    return None
def solution(begin, target, words):
    graph = defaultdict(list)
    make_graph(begin, words, graph)
    for word in words:
        make_graph(word,words, graph)
    queue = deque()
    queue.append((begin, 0))
    visited = []
    while queue:
        current, distance = queue.popleft()
        visited.append(current)
        for node in graph[current]:
            if node not in visited:
                queue.append((node, distance+1))
                if node == target:
                    return distance+1

    return 0
