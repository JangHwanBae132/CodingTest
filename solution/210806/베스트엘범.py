def solution(genres, plays):
    answer = []
    totalDic = {}
    playDic = {}

    totalPlayCount(genres, plays, totalDic, playDic)

    sortedArr = sorted(totalDic.items(), key=lambda x: x[1], reverse=True)

    for a in sortedArr:
        for aa in playDic[a[0]]:
            answer.append(aa[0])

    return answer


def totalPlayCount(genres, plays, totalDic, playDic):
    for i in range(len(genres)):
        print(i)
        if genres[i] not in totalDic.keys():
            totalDic[genres[i]] = plays[i]
            arr= [[]]
            arr[0] = [i,plays[i]]
            playDic[genres[i]] = arr
        else:
            totalDic[genres[i]] += plays[i]
            if plays[i] > playDic[genres[i]][0][1]:
                playDic[genres[i]] = [[i, plays[i]], [playDic[genres[i]][0][0], playDic[genres[i]][0][1]] ]
            elif len(playDic[genres[i]]) ==1:
                playDic[genres[i]].append([i, plays[i]])
            elif playDic[genres[i]][0][1] >= plays[i] > playDic[genres[i]][1][1]:
                playDic[genres[i]] = [[playDic[genres[i]][0][0], playDic[genres[i]][0][1]], [i, plays[i]] ]
