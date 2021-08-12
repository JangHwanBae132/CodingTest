def solution(s):
    answer = []
    s = s[2:len(s) - 2]
    ls = s.split("},{")
    ls.sort(key=len)
    for ss in ls:
        for i in ss.split(","):
            if int(i) not in answer:
                answer.append(int(i))
    print(answer)
    return answer
