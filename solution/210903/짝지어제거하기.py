from collections import deque

def solution(s):

    stack = []
    queue = deque(list(s))

    while queue:
        que_pop = queue.popleft()
        if len(stack) ==0:
            stack.append(que_pop)
        elif stack[-1] == que_pop:
            stack.pop()
        else:
            stack.append(que_pop)

    if len(stack) ==0:
        return 1
    else:
        return 0
