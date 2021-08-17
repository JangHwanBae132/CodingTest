def solution(files):
    answer = []
    dic = {}
    for f in files:
        head = "";
        number = "";
        isNum = False
        for a in list(f):
            if not a.isdigit() and not isNum:
                head += a.lower()
            elif a.isdigit() and not isNum:
                isNum = True
                number += a
            elif a.isdigit() and isNum:
                number +=a
            elif not a.isdigit() and isNum:
                break
        dic[f] = [head, int(number)]

    print(dic)
    sortedDic1 = sorted(dic.items(), key=lambda x: x)
    print(sortedDic1)
    sortedDic2 = sorted(sortedDic1, key=lambda x: x[1][0])
    print(sortedDic2)

    for d in sortedDic2:
        answer.append(str(d[0]))

    print(answer)
    return answer
