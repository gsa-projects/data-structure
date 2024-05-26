def insertion_sort(A):
    for i in range(1, len(A) - 1):
        for j in range(i, 0, -1):
            if A[j - 1] > A[j]:
                A[j], A[j - 1] = A[j - 1], A[j]

A = [54, 88, 77, 26, 93, 17, 49, 10, 17, 77, 11, 31, 22, 44, 17, 20]
print(A)
insertion_sort(A)
print(A)
