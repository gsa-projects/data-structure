def knapsack(wgt, val, W):
    # 단위 무게 당 가치로 정렬시키기
    z = list(zip(wgt, val))
    z.sort(key=lambda t: t[1]/t[0], reverse=True)
    wgt, val = list(zip(*z))
    
    # 그리디
    n = len(wgt)
    s = 0
    for i in range(n):
        if W <= 0:
            break   
        elif W >= wgt[i]:   # 다 넣을 수 있으면
            W -= wgt[i]
            s += val[i]
        else:
            s += val[i] * W/wgt[i]  # 부분만 넣을 수 있으면
            W = 0
            break
    
    return s
    
if __name__ == "__main__":
    print(knapsack([10, 12, 8], [80, 120, 60], 18))
