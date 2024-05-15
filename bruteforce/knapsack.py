def knapsack(weights, values, weight):
    n = len(weights)
    best_val = 0

    for i in range(2 ** n):
        s = [0] * n

        for d in range(n):
            s[d] = i % 2
            i //= 2

        sum_val = 0
        sum_weight = 0
        for d in range(n):
            if s[d] == i:
                sum_weight += weights[d]
                sum_val += values[d]

        if sum_weight <= weight:
            if sum_val > best_val:
                best_val = sum_val

    return best_val


if __name__ == '__main__':
    print(knapsack([10, 20, 30, 25, 35], [60, 100, 120, 70, 85], 80))
