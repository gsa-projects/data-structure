from collections import defaultdict

dp = defaultdict(int)

# 메모이제이션 (탑다운)
def fib(n):
    if n <= 1:
        return n
    
    if dp[n]:
        return dp[n]
    
    dp[n] = fib(n - 1) + fib(n - 2)
    return dp[n]

for i in range(40):
    print(fib(i), end=' ')
    
print()
dp2 = defaultdict(int)

# 타뷸레이션 (바텀엄)
def fib2(n):
    dp2[0] = 0
    dp2[1] = 1
    
    for i in range(2, n + 1):
        dp2[i] = dp2[i - 1] + dp2[i - 2]
    
    return dp2[n]

print(fib(39))