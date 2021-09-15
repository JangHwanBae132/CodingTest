def solution(n):
    answer =0
    temp_n_minus1 = 2
    temp_n_minus2 = 1

    if n ==1 :
        return 1

    if n ==2:
        return 2

    for i in range(2, n):
        answer = (temp_n_minus1 + temp_n_minus2)%1000000007
        if i == n-1:
            break
        else:
            temp_n_minus2 = temp_n_minus1
            temp_n_minus1 = answer

    return answer
