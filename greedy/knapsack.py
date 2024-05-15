def knapsack(weights, values, W):
    best_val = 0

    for i in range(len(weights)):
        if W <= 0:
            break
        elif W >= weights[i]:
            W -= weights[i]
            best_val += values[i]
        else:
            frac = W / weights[i]
            best_val += values[i] * frac
            break

    return best_val


if __name__ == "__main__":
    print(knapsack([12, 10, 8], [120, 80, 60], 18))
