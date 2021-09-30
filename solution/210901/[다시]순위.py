def solution(n, results):
    answer = 0

    win_dic = dict()
    lose_dic = dict()
    for i in range(n):
        win_dic[i+1] = set()
        lose_dic[i+1] = set()

    for result in results:
        winner = result[0]
        loser = result[1]

        win_dic[winner].add(loser)
        win_dic[winner].update(win_dic[loser])
        for winner_of_winner in lose_dic[winner]:
            win_dic[winner_of_winner].update(win_dic[winner])

        lose_dic[loser].add(winner)
        lose_dic[loser].update(lose_dic[winner])
        for loser_of_loser in win_dic[loser]:
            lose_dic[loser_of_loser].update(lose_dic[loser])

    # print(win_dic)
    # print(lose_dic)

    for i in range(n):
        if len(win_dic[i + 1])+len(lose_dic[i + 1]) == n-1:
            answer+=1

    return answer
