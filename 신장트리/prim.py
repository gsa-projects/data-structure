import sys
INF = 999

# MST = Minimum Spanning Tree, 최소 비용 신장 트리
# prim은 정점 중심으로 최소 신장 트리를 찾아나간다. O(ElogV)
def prim(vtx, adj, start):
    n = len(vtx)
    selected = [False] * n
    D = [INF] * n
    D[start] = 0
    
    for _ in range(n):  # n개의 정점을 지나서 MST에 넣어야 종료
        u = get_min_vtx(D, selected, start)
        selected[u] = True
        print(vtx[u], end=' ')
        
        for v in range(n):
            if adj[u][v] != INF:
                if not selected[v]: # 그리디하게
                    D[v] = min(D[v], adj[u][v])
                    
        print(D)    # 중간 결과 출력
        

def get_min_vtx(D, selected, start):
    min_dist = INF
    min_idx = start
    
    for v in range(len(D)):
        if selected[v] == False and min_dist > D[v]:
            min_dist = D[v]
            min_idx = v
            
    return min_idx

vertex = ["A", "B", "C", "D", "E", "F", "G"]
matrix = [
    [INF, 25, INF, 12, INF, INF, INF],
    [25, INF, 10, INF, 15, INF, INF],
    [INF, 10, INF, INF, INF, INF, 16],
    [12, INF, INF, INF, 17, 37, INF],
    [INF, 15, INF, 17, INF, 19, 14],
    [INF, INF, INF, INF, 14, INF, 42],
    [INF, INF, 16, 37, 14, 42, INF],
]

prim(vertex, matrix, 0)