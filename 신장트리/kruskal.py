# kruskal은 간선 중심으로 최소 신장 트리를 찾아나간다. O(ElogE)
weights = [(0, 1, 9), (0, 2, 10), (1, 3, 10), (1, 4, 5),
           (1, 6, 3), (2, 3, 9), (2, 4, 7), (2, 5, 2),
           (3, 5, 4), (3, 6, 8), (4, 6, 1), (5, 6, 6)]
weights.sort(key=lambda t: t[2], reverse=True)    # 가중치 작은 순서대로 정렬

mst = []    # 최소 신장 트리
N = 7   # 정점 갯수
parents = list(range(N))

def find(u):
    if u != parents[u]:
        parents[u] = find(parents[u])
    return parents[u]

def union(u, v):
    u = find(u)
    v = find(v)
    
    parents[v] = u
    
cnt = 0
cost = 0

while cnt < N - 1:  # 정점이 N개면 최소 신장 트리의 간선은 N - 1개.
    u, v, wgt = weights.pop()
    
    if find(u) != find(v):
        union(u, v)
        mst.append((u, v))  # 그리디하게
        cost += wgt
        cnt += 1
    
print(mst)
print(cost)