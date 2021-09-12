def solution(N, road, K):
    answer = 0

    graph_map = [[0 if i ==j else K+1 for i in range(N)] for j in range(N)]
    visited = [0]

    for r in road:
        if r[2] <= graph_map[r[0]-1][r[1]-1]:
            graph_map[r[0]-1][r[1]-1] = r[2]
            graph_map[r[1]-1][r[0]-1] = r[2]
        else:
            continue

    while True:
        visit_min = K+1
        next_node = -1
        for node, node_value in enumerate(graph_map[0]):
            if node not in visited and node_value < visit_min:
                next_node = node
                visit_min = node_value

        if next_node == -1:
            break


        for i  in range(0, len(graph_map[next_node])):
            if graph_map[0][next_node] + graph_map[next_node][i] < graph_map[0][i]:
                graph_map[0][i]= graph_map[0][next_node] + graph_map[next_node][i]
                graph_map[i][0]= graph_map[0][next_node] + graph_map[next_node][i]

        visited.append(next_node)

    for g in graph_map[0]:
        if g <=K:
            answer +=1
    return answer
