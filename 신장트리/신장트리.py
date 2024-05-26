def ST_DFS(vtx, adj, start, visited):   # 연결 성분을 구할 수 있으나 최소임을 보장할 수 없음.
    visited[start] = True
    
    for v in range(len(vtx)):
        if adj[start][v] != 0:
            if not visited[v]:
                print(f'({vtx[start]}, {vtx[v]})', end=' ')
                ST_DFS(vtx, adj, v, visited)
                
vtx = ["U", "V", "W", "X", "Y"]
adj = [
    [0, 1, 1, 0, 0],
    [1, 0, 1, 1, 0],
    [1, 1, 0, 0, 1],
    [0, 1, 0, 0, 0],
    [0, 0, 1, 0, 0],
]
visited = [False] * 5

ST_DFS(vtx, adj, 0, visited)
"""
U     W --- Y
|   / 
| /   
V --- X
"""