def knapsack(wgt, val, W):  # O(2^n)
    n = len(wgt)
    best = -1
    
    for i in range(2**n):
        s = [0] * n
        for j in range(n):
            s[j] = i % 2
            i //= 2
        
        w, v = 0, 0
        for j in range(n):
            if s[j] == 1:
                w += wgt[j]
                v += val[j]
        
        if w <= W:
            best = max(best, v)
    
    return best

# 더 빠르게 푸려면 dp를 써야 하는데 시험 범위가 아니므로.

if __name__ == '__main__':
    print(knapsack([10, 20, 30, 25, 35], [60, 100, 120, 70, 85], 80))
