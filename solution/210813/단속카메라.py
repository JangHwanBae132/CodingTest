def solution(routes):
    answer = 1
    sortRoutes = sorted(routes, key=lambda x: x[0])
    temp = sortRoutes[0]
    for i in range(len(sortRoutes)-1):
        if(temp[1] < sortRoutes[i+1][0]):
            answer +=1
            temp = sortRoutes[i+1]
        else:
            if(temp[1]> sortRoutes[i+1][1]):
                temp = sortRoutes[i+1]
            else:
                temp = [sortRoutes[i+1][0], temp[1]]

    return answer
