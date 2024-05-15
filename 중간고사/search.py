def binary_search(A, key, low, high):
    if low <= high:
        mid = (low + high) // 2

        if A[mid] == key:
            return mid
        elif A[mid] < key:
            return binary_search(A, key, mid + 1, high)
        else:
            return binary_search(A, key, low, mid - 1)

    return -1

def binary_search_loop(A, key, low, high):
    while low <= high:
        mid = (low + high) // 2

        if key == A[mid]:
            return mid
        elif key < A[mid]:
            high = mid - 1
        else:
            low = mid + 1

    return -1

if __name__ == '__main__':
    A = list(range(3, 50, 2))

    print(A)
    print(17, binary_search(A, 17, 0, len(A) - 1))
    print(17, binary_search_loop(A, 17, 0, len(A) - 1))
