import itertools


def solution(relation):

    answer_list = []
    columns = []

    number = [i for i in range(len(relation[0]))]

    for i in range(len(relation[0])):
        columns.append(list(zip(*relation))[i])


    for i in range(len(relation[0])):
        # print(number)
        if i >= len(number):
            break
        comb = itertools.combinations(number, i + 1)
        for c in list(comb):
            hashset =set()
            zip_comb = []
            for cc in c:
                zip_comb.append(columns[cc])

            for j in range(len(columns[0])):
                hashset.add(list(zip(*zip_comb))[j])

            # print(hashset)
            if len(hashset) == len(relation):
                isAnswer = True
                for a in answer_list:
                    same_count =0
                    for aa in a:
                        if aa in c:
                            same_count +=1
                    if same_count == len(a):
                        isAnswer = False
                        break
                if isAnswer:
                    answer_list.append(c)

    return len(answer_list)
