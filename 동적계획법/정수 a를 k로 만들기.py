import sys
a, k = map(int, input().split())

INF = sys.maxsize
DP = [INF] * (k + 1)
DP[a] = 0

# me
for i in range(a + 1, k + 1):
    if i % 2 == 0 and i // 2 >= a:
        DP[i] = min(DP[i - 1], DP[i // 2]) + 1
    else:
        DP[i] = DP[i - 1] + 1

print(DP[k])

# teacher
D = [0] * (k + 1)
for i in range(a + 1, k + 1):
    D[i] = D[i - 1] + 1
    
    if i % 2 == 0 and i // 2 >= a:
        D[i] = min(D[i], D[i // 2] + 1)

print(D[k])

# 최소 연산의 경로까지 구하는 방법 -> 동적계획법의 역추적
path = []
D = [0] * (k + 1)
for i in range(a + 1, k + 1):
    D[i] = D[i - 1] + 1
    
    if i % 2 == 0 and i // 2 >= a:
        D[i] = min(D[i], D[i // 2] + 1)

now = k
while now > a:
    path.append(now)
    
    if now % 2 == 0 and now // 2 >= a and D[now // 2] < D[now - 1]:
        now //= 2
    else:
        now -= 1

path.append(a)
path.reverse()
print(path)