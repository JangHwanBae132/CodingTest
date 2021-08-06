def solution(clothes):
    answer = 0
    dic = {}
    makeDic(dic, clothes)
    answer = 1;
    answer = makeAnswer(answer, dic)-1
    return answer


def makeDic(dic, clothes):
    for c in clothes:
        if c[1] not in dic.keys():
            dic[c[1]] = [c[0]]
        else:
            dic[c[1]].append(c[0])


def makeAnswer(answer, dic):
    for key in dic.keys():
        answer *= len(dic[key])+1;

    return answer
