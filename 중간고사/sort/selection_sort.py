def selection_sort(A):
    for i in range(len(A) - 1):
        min_idx = i

        # for j in range(i, len(A)):
        #     if A[min_idx] > A[j]:
        #         min_idx = j
        min_idx = min(range(i, len(A)), key=lambda k: A[k])

        A[min_idx], A[i] = A[i], A[min_idx]

A = [54, 88, 77, 26, 93, 17, 49, 10, 17, 77, 11, 31, 22, 44, 17, 20]
print(A)
selection_sort(A)
print(A)
