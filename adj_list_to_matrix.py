def adjacency_list_to_matrix(adjacency_list):
    n = len(adjacency_list)
    
    matrix = [[0 for j in range(n)] for i  in range(n)]

    for node, neighbors in adjacency_list.items():
        for neighbor in neighbors:
            matrix[node][neighbor] = 1

    for row in matrix:
        print(row)
    return matrix

adjacency_list_to_matrix({0: [2], 1: [2, 3], 2: [0, 1, 3], 3: [1, 2]})
print()
adjacency_list_to_matrix({0: [1], 1: [0]})