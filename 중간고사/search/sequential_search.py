def sequential_search(A, key, low, high):
    for i in range(low, high + 1):
        if key == A[i]:
            return i
    return -1

def sequential_search_transpose(A, key, low, high):
    for i in range(low, high + 1):
        if key == A[i]:
            if i > low:     # 맨 처음 요소가 아니여야 스왑할 때 low - 1를 가져오는 문제 안 생김
                A[i], A[i - 1] = A[i - 1], A[i]
                i = i - 1
            return i
    return -1

if __name__ == "__main__":
    A = [1, 2, 3, 4, 5, 6, 7, 8]

    print(A)
    print(sequential_search(A, 3, 0, len(A) - 1))

    print()

    print(A)
    print(sequential_search_transpose(A, 5, 0, len(A) - 1))
    print(A)
