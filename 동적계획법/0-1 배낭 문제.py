cargo = [(4, 12), (2, 1), (10, 4), (1, 1), (2, 2)]  # (val, wgt)
n = len(cargo)
w = 15
DP = [[0] * (w + 1) for _ in range(n + 1)]   # D[개수][여유용량], 물건은 순서대로만 넣을 수 있음

val, wgt = list(zip(*cargo))

# me
for i in range(n + 1):
    for j in range(w + 1):
        if i == 0 or j == 0:
            DP[i][j] = 0
        elif wgt[i - 1] <= j:
            DP[i][j] = max(DP[i - 1][j], DP[i - 1][j - wgt[i - 1]] + val[i - 1])
        else:
            DP[i][j] = DP[i - 1][j]

# teacher
capacity = 15
dp = []

for i in range(len(cargo) + 1):
    dp.append([])
    for j in range(capacity + 1):
        if i == 0 or j == 0:
            dp[i].append(0)
        elif cargo[i - 1][1] <= j:
            dp[i].append(max(cargo[i - 1][0] + dp[i - 1][j - cargo[i - 1][1]], dp[i - 1][j]))
        else:
            dp[i].append(dp[i - 1][j])

print(DP[n][w])
print(dp[n][w])