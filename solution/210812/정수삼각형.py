def solution(triangle):
    answer = 0
    for i in range(len(triangle)-1, 0, -1):
        for j in range(0, i):
            triangle[i-1][j] = triangle[i-1][j]+triangle[i][j] if triangle[i][j]>triangle[i][j+1] else triangle[i-1][j]+triangle[i][j+1]

    return triangle[0][0]
