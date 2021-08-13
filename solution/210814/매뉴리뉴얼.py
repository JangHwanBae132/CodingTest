from itertools import combinations


def solution(orders, course):
    answer = []
    arr = makeArrSet(orders)
    for c in course:
        dic = {}
        t = False
        for a in arr:
            if len(a)>=c:
                t = True
                for o in list(combinations(a,c)):
                    if o in dic.keys():
                        dic[o] +=1
                    else:
                        dic[o] =1
        if t:
            sortDic = sorted(dic.items(), key=lambda x: x[1], reverse=True)
            key = sortDic[0][1]
            if key >1:
                for i in range(len(sortDic)):
                    if sortDic[i][1] == key:
                        answer.append(''.join(list(sortDic[i][0])))
                    else:
                        break

    return sorted(answer)

def makeArrSet(orders):
    arr = []
    for o in orders:
        l = sorted(list(o))
        arr.append(l)

    sortedArr = sorted(arr, key=len)
    return sortedArr
