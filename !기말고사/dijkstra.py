import sys

inf = sys.maxsize
graph = [
    [(1, 1), (3, 2)],
    [(0, 1), (2, 4), (3, 3), (4, 1), (5, 6)],
    [(1, 4), (5, 1), (6, 1), (7, 2)],
    [(0, 2), (1, 3), (4, 5)],
    [(1, 1), (3, 5), (6, 2)],
    [(1, 6), (2, 1), (7, 9)],
    [(2, 1), (4, 2), (7, 1)],
    [(2, 2), (5, 9), (6, 1)]
]
start = 0
N = len(graph)

previous = [None] * N
previous[start] = start

visited = [False] * N
# visited[start] = True 이거 미리 하면 안됨. min_vertex 찾게 냅둬야 함. 어차피 첫 min_vertex는 항상 start랑 같음. 처음에 이게 True면 나머지 D가 전부 inf라서 min_vertex 탐색이 안됨.

D = [inf] * N
D[start] = start

for _ in range(N):
    min_dist = inf
    min_vertex = -1
    for i in range(N):
        if not visited[i] and D[i] < min_dist:
            min_dist = D[i]
            min_vertex = i
            
    visited[min_vertex] = True
    for w, d in graph[min_vertex]:
        if not visited[w]:
            if D[w] > D[min_vertex] + d:
                D[w] = D[min_vertex] + d
                previous[w] = min_vertex

print(visited)

for i, v in enumerate(D):
    print(f"({start}, {i}) = {v}")
    
for i in range(N):
    cur = i
    print(cur, end='')
    while cur != start:
        cur = previous[cur]
        print(f" <- {cur} ", end='')
    print()