import sys
INF = sys.maxsize
N = 8

g = [None] * N
g[0] = [(1, 1), (3, 2)]
g[1] = [(0, 1), (2, 4), (3, 3), (4, 1), (5, 6)]
g[2] = [(1, 4), (5, 1), (6, 1), (7, 2)]
g[3] = [(0, 2), (1, 3), (4, 5)]
g[4] = [(1, 1), (3, 5), (6, 2)]
g[5] = [(1, 6), (2, 1), (7, 9)]
g[6] = [(2, 1), (4, 2), (7, 1)]
g[7] = [(2, 2), (5, 9), (6, 1)]

"""
다익스트라 알고리즘도 그리디한 알고리즘이다. MST의 Prim 알고리즘과 유사하다.
차이점:
- 다익스트라 알고리즘은 출발점이 있지만, 프림 알고리즘은 임의의 점에서 출발.
- 프림 알고리즘에서는 D에 간선의 가중치를 저장, 다익스트라 알고리즘에서는 D에 출발점으로부터의 간선의 가중치의 합(거리)를 저장

다익스트라 알고리즘이 최적해를 찾지 못하는 반례:
음수 가중치가 존재하면 D의 가중치의 증가 순으로 min vertex를 선택하고, 한 번 방문된 정점의 D 원소를 다시 갱신하지 않기 때문 TODO: 뭐라노.
"""

# TODO: 여기 복습

visited = [False] * N
start = 0
D = [INF] * N
D[start] = 0

previous = [None] * N
previous[start] = start

for k in range(N):
    m = -1
    min_value = INF

    for j in range(N):
        if not visited[j] and D[j] < min_value:
            min_value = D[j]
            m = j
    visited[m] = True

    for v, wt in list(g[m]):
        if not visited[v]:
            if D[m] + wt < D[v]:
                D[v] = D[m] + wt
                previous[v] = m

print('정점', start, '로부터 최단 거리: ')
for i in range(N):
    if D[i] == sys.maxsize:
        print(start, '와', i, '사이에 경로 없음')
    else:
        print(f'[{start}, {i}] = {D[i]}')

print('\n정점', start, '으로부터의 최단 거리: ')
for i in range(N):
    back = i
    print(back, end='')

    while back != start:
        print(' <-', previous[back], end='')
        back = previous[back]
    print()
