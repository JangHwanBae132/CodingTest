def solution(word):
    answer = 0
    weight = {"A": 0, "E": 1, "I": 2, "O": 3, "U": 4}
    word_list = list(word)

    for i, w in enumerate(word_list):
        answer+=1
        for j in range(5-i):
            answer += (5**j)*weight[w]
    return answer
