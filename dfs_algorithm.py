def dfs(adj_matrix, start_node):
    visited = []
    stack = [start_node]
    seen = set()

    while stack:
        current = stack.pop()
        if current not in seen:
            seen.add(current)
        #if not visited:
            visited.append(current)
            n = len(adj_matrix)
            for i, connected in enumerate(adj_matrix[current]):
                if connected == 1 and i not in seen:
                    stack.append(i)
    return visited

print(dfs([[0, 1, 0, 0], [1, 0, 1, 0], [0, 1, 0, 1], [0, 0, 1, 0]], 1))
print(dfs([[0, 1, 0, 0], [1, 0, 1, 0], [0, 1, 0, 0], [0, 0, 0, 0]], 3))