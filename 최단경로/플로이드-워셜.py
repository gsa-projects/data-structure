import sys

N = 5
INF = sys.maxsize
# 플로이드 워셜 알고리즘은 인접 행렬을 사용, INF는 연결되지 않은 것을 의미.
D = [[0, 4, 2, 5, INF],
     [INF, 0, 1, INF, 4],
     [1, 3, 0, 1, 2],
     [-2, INF, INF, 0, 2],
     [INF, -3, 3, 1, 0]]

for k in range(N):  # k가 제일 먼저 나오는 반복문임에 주의.
    for i in range(N):
        for j in range(N):
            D[i][j] = min(D[i][j], D[i][k] + D[k][j])   # k를 거치고 오는 경로.
            
for d in D:
    print(d)