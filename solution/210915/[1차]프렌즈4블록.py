def solution(m, n, board):
    answer = 0
    board_map = [[board[i][j] for j in range(n)] for i in range(m)]

    while True:
        delete_set = delete_4block(m, n, board_map)
        # print(board_map)
        # print(delete_set)
        if len(delete_set) ==0:
            break
        else:
            board_map= rearrange(m, n, board_map, delete_set)
            answer += len(delete_set)
    return answer

def delete_4block(m, n, board_map):
    delete_set = set()
    for i in range(m-1):
        for j in range(n-1):
            if board_map[i][j] != "0" and board_map[i][j] == board_map[i+1][j] and board_map[i][j] == board_map[i+1][j] and  board_map[i][j] == board_map[i][j+1] and board_map[i][j] == board_map[i+1][j+1]:
                delete_set.add((i, j))
                delete_set.add((i+1, j))
                delete_set.add((i, j+1))
                delete_set.add((i+1, j+1))

    return delete_set


def rearrange(m, n, board_map, delete_set):
    for j in range(n):
        stack = []
        for i in range(m):
            if (i, j) not in delete_set:
                stack.append(board_map[i][j])
        for i in range(m-1, -1,-1):
            if len(stack) !=0:
                pop = stack.pop()
                board_map[i][j] =pop
            else:
                board_map[i][j] = "0"
    return board_map
