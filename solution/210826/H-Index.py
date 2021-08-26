def solution(citations):
    answer = 0
    citations.sort(reverse=True)
    if citations[1] == 0:
        return 0
    for h in range(len(citations)):
        if h+1 <= citations[h] and h > answer:
            answer= h
    return answer+1
