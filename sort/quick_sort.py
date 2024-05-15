def quick_sort(A, low, high):
    if low < high:
        pivot = partition(A, low, high)
        quick_sort(A, low, pivot - 1)
        quick_sort(A, pivot + 1, high)

def partition(A, low, high) -> int:
    i = low + 1
    j = high

    while True:
        while i < high and A[i] < A[low]:
            i += 1
        while low < j and A[low] < A[j]:
            j -= 1

        if j <= i:
            break

        A[i], A[j] = A[j], A[i]
        i += 1
        j -= 1

    A[low], A[j] = A[j], A[low]
    return j

A = [54, 88, 77, 26, 93, 17, 49, 10, 17, 77, 11, 31, 22, 44, 17, 20]
print(A)
quick_sort(A, 0, len(A) - 1)
print(A)