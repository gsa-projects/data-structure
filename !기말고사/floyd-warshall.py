import sys

inf = sys.maxsize
D = [[0, 4, 2, 5, inf],
     [inf, 0, 1, inf, 4],
     [1, 3, 0, 1, 2],
     [-2, inf, inf, 0, 2],
     [inf, -3, 3, 1, 0]]
N = len(D)

for k in range(N):
    for i in range(N):
        for j in range(N):
            if D[i][j] > D[i][k] + D[k][j]:
                D[i][j] = D[i][k] + D[k][j]

for d in D:
    print(d)
