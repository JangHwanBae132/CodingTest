from collections import deque


def solution(p):
    answer =dp(p)
    return answer

def dp(p):
    if p == "":
        return ""

    cnt =1
    stack = []
    queue = deque(list(p))

    stack.append(queue.popleft())

    while stack:
        pop = queue.popleft()
        cnt +=1
        if stack[-1] != pop:
            stack.pop()
        else:
            stack.append(pop)

    queue.clear()
    u = p[:cnt]

    v = p[cnt:]

    if u[:1] == "(":
        return u+dp(v)
    else:
        new_u = ""
        for _u in list(u[1:-1]):
            if _u == "(":
                new_u += ")"
            else:
                new_u += "("

        return "("+dp(v)+")"+new_u
