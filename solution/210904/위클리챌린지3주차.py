from collections import deque


def solution(game_board, table):
    answer = 0
    blocks = find_block(table, 1)
    blanks = find_block(game_board, 0)

    normalized_blocks = normalizing(blocks)

    rotate_blacks_dic = rotate_dic(blanks)

    for block in blocks:
        for key in rotate_blacks_dic.keys():
            if block in rotate_blacks_dic[key]:
                answer+= len(block)
                rotate_blacks_dic.pop(key)
                break

    return answer

def rotate_dic(blanks):
    dic = {}
    for i, blank in enumerate(blanks):
        rotate_blank = []
        rotate_blank.append(blank)
        rotate_blank.append(rotate(rotate_blank[-1]))
        rotate_blank.append(rotate(rotate_blank[-1]))
        rotate_blank.append(rotate(rotate_blank[-1]))
        dic[i] = normalizing(rotate_blank)

    return dic

def rotate(blank):
    rotate_blank = []
    for (x, y) in blank:
        rotate_blank.append([y,-x])
    return rotate_blank

def find_block(table, number):
    visited = table.copy()
    blocks = []
    for i in range(len(visited)):
        for j in range(len(visited)):
            if visited[i][j] == number:
                block = bfs_find_block([i,j], number, visited)
                blocks.append(block)
    return blocks

def bfs_find_block(start, number, visited):
    if number == 0:
        _num =1
    elif number ==1:
        _num =0

    block = []
    queue =deque()
    queue.append(start)
    visited[start[0]][start[1]] = _num

    while queue:
        popleft = queue.popleft()
        block.append(popleft)

        if popleft[0] > 0 and visited[popleft[0]-1][popleft[1]] == number:
            queue.append([popleft[0]-1, popleft[1]])
            visited[popleft[0] - 1][popleft[1]] = _num

        if popleft[0] < len(visited)-1 and visited[popleft[0]+1][popleft[1]] == number:
            queue.append([popleft[0]+1, popleft[1]])
            visited[popleft[0]+1][popleft[1]] = _num

        if popleft[1] > 0 and visited[popleft[0]][popleft[1]-1] == number:
            queue.append([popleft[0], popleft[1]-1])
            visited[popleft[0]][popleft[1]-1] = _num

        if popleft[1] < len(visited)-1 and visited[popleft[0]][popleft[1]+1] == number:
            queue.append([popleft[0], popleft[1]+1])
            visited[popleft[0]][popleft[1]+1] = _num

    return block

def normalizing(blocks):
    for b in blocks:
        x_min = min(list(zip(*b))[0])
        y_min = min(list(zip(*b))[1])
        for bb in b:
            bb[0] += -x_min
            bb[1] += -y_min
        b.sort(key= lambda x: x[1])
        b.sort(key= lambda x: x[0])
    return blocks
