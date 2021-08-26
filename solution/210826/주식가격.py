def solution(prices):
    answer = [len(prices)-i-1 for i in range(len(prices))]
    stack = []
    for i, p in enumerate(prices):
        while stack:
            print(stack)
            if stack[-1][0] > p:
                pop = stack.pop()
                answer[pop[1]] = i-pop[1]
            else:
                break
        stack.append([p, i])

    print(answer)
    return answer
