def solution(places):
    answer = []
    for place in places:
        breaking = False
        for i in range(5):
            for j in range(5):
                p_list = []
                if j < 3:
                    p_list.append(place[i][j:j+3])
                if i < 3:
                    p_list.append(place[i][j:j+1]+place[i+1][j:j+1]+place[i+2][j:j+1])
                if i < 4 and j < 4:
                    p_list.append(place[i][j:j+2]+place[i+1][j+1:j+2])
                    p_list.append(place[i][j:j+1]+place[i+1][j:j+2])
                    p_list.append(place[i+1][j:j+1]+place[i][j:j+2])
                    p_list.append(place[i+1][j:j+2]+place[i][j+1:j+2])
                for p in p_list:
                    if p[:2] =="PP" or p[1:] =="PP" or p =="POP":
                        breaking = True
                        break

                if breaking:
                    break
            if breaking:
                break
        if breaking:
            answer.append(0)
        else:
            answer.append(1)

    return answer
