from collections import deque


def check(s):
    queue = deque(list(s))
    stack = []
    stack.append(queue.popleft())
    while queue:
        if len(stack) >0 and (stack[0] == ")" or stack[0] == "}" or  stack[0] == "]"):
            return 0
        pop = queue.popleft()
        if len(stack) >0 and check_bracket(stack[-1], pop):
            stack.pop()
        else:
            stack.append(pop)

    if len(stack)== 0:
        return 1
    else:
        return 0

def check_bracket(start, end):
    if start == "(" and end == ")":
        return True
    if start == "{" and end == "}":
        return True
    if start == "[" and end == "]":
        return True
    return False



def solution(s):
    answer = 0
    l = len(s)
    for i in range(l):
        answer += check(s)
        s = s[1:]+s[0]
    return answer
