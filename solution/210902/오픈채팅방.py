def solution(record):
    id_nickname ={}

    temp_ans = []
    answer = []

    for r in record:
        split_r = r.split(" ")

        if split_r[0] == "Enter":
            id_nickname[split_r[1]] = split_r[2]
            temp_ans.append([1, split_r[1]])
        elif split_r[0] == "Leave":
            temp_ans.append([-1, split_r[1]])
        elif split_r[0] == "Change":
            id_nickname[split_r[1]] = split_r[2]


    for a in temp_ans:
        if a[0] == 1:
            answer.append(id_nickname[a[1]]+"님이 들어왔습니다.")
        elif a[0] == -1:
            answer.append(id_nickname[a[1]]+"님이 나갔습니다.")

    return answer
