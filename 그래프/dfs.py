def dfs(vtx, adj, s, visited):
    print(vtx[s], end=' ')
    visited[s] = True

    for v in range(len(vtx)):
        if adj[s][v] != 0:
            if not visited[v]:
                dfs(vtx, adj, v, visited)

vtx = ['U', 'V', 'W', 'X', 'Y']
edge = [[0, 1, 1, 0, 0],
        [1, 0, 1, 1, 0],
        [1, 1, 0, 0, 1],
        [0, 1, 0, 0, 0],
        [0, 0, 1, 0, 0]]

print("dfs (start: U):", end=' ')
dfs(vtx, edge, 0, [False] * len(vtx))
