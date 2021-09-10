# 문제에 오해의 소지가 있음 => 말에 따라 2가지 경우로 해석될 수 있는데 이에 대한 명확한 구분이 안 되어 있음

def solution(enroll, referral, seller, amount):
    answer = [0 for i in range(len(enroll))]

    index = {}
    for i in range(len(enroll)):
        index[enroll[i]] = i

    for i, se in enumerate(seller):
        ref = referral[index[se]]
        money = amount[i]*100
        answer[index[se]] += money - int(money*0.1)
        money = int(money*0.1)
        while ref !="-":
            answer[index[ref]] += money - int(money*0.1)
            money = int(money * 0.1)
            if money == 0:
                break
            ref = referral[index[ref]]

    return answer
