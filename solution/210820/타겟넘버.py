def solution(numbers, target):
    answer = 0
    answer = dfs(numbers, target, 0, 0)
    print(answer)
    return answer

def dfs(numbers, target,  i , result):
    if i== len(numbers):
        if result == target:
            return 1
        else:
            return 0
    else:
       return dfs(numbers, target, i+1, result+numbers[i])+dfs(numbers, target, i+1, result-numbers[i])
