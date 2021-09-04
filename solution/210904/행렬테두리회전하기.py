def solution(rows, columns, queries):
    array = [[col+row*columns+1 for col in range(columns)] for row in range(rows)]
    answer = []
    for query in queries:
        answer.append(rotate(array, query))
    return answer

def rotate(array, query):
    min_value= 0
    arr =[]
    temp = array[query[0]-1][query[1]-1]
    arr.append(temp)
    for i in range(query[1], query[3]):
        _temp = array[query[0]-1][i]
        array[query[0]-1][i] = temp
        temp = _temp
        arr.append(temp)

    for i in range(query[0], query[2]):
        _temp = array[i][query[3]-1]
        array[i][query[3]-1] = temp
        temp = _temp
        arr.append(temp)

    for i in range(query[3]-2, query[1]-1, -1):
        _temp = array[query[2]-1][i]
        array[query[2]-1][i] = temp
        temp = _temp
        arr.append(temp)

    for i in range(query[2]-1, query[0]-1, -1):
        _temp = array[i][query[1]-1]
        array[i][query[1]-1] = temp
        temp = _temp
        arr.append(temp)

    array[query[0] - 1][query[1] - 1] =temp

    min_value = min(arr)
    return min_value
