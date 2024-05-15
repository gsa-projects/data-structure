import pytest
import random

#%% Selection Sort
def selection_sort(A, low, high):
    for i in range(len(A) - 1):
        min_idx = i
        for j in range(i + 1, len(A)):
            if A[j] < A[min_idx]:     # TODO: A[j] < A[i] 라고 씀
                min_idx = j
        
        A[min_idx], A[i] = A[i], A[min_idx]
#%% Insertion Sort
def insertion_sort(A, low, high):
    for i in range(1, len(A)):
        for j in range(i, 0, -1):
            if A[j - 1] > A[j]:
                A[j - 1], A[j] = A[j], A[j - 1]
#%% Heap Sort
def downheap(H, i, size):
    while 2*i <= size:
        max_child = 2*i

        if 2*i + 1 <= size:
            if H[2*i + 1] > H[max_child]:
                max_child = 2*i + 1
        
        if H[i] >= H[max_child]:
            break

        H[i], H[max_child] = H[max_child], H[i]
        i = max_child

def heapify(A):
    size = len(A) - 1

    for i in range(size // 2, 0, -1):
        downheap(A, i, size)
    
    return A

def heap_sort(A, low, high):
    size = len(A) - 1

    for _ in range(size):
        A[1], A[size] = A[size], A[1]
        size -= 1
        downheap(A, 1, size)
#%% Quick Sort
def quick_sort(A, left, right):
    if left < right:
        p = partition(A, left, right)
        quick_sort(A, left, p - 1)
        quick_sort(A, p + 1, right)

def partition(A, left, right):
    pivot = A[left]
    low = left
    high = right

    while low <= high:
        while low <= right and A[low] <= pivot:
            low += 1
        while left <= high and pivot < A[high]:
            high -= 1
        
        if low < high:
            A[low], A[high] = A[high], A[low]
    
    A[left], A[high] = A[high], A[left]
    return high
#%%

@pytest.mark.parametrize("f", [
    selection_sort,
    insertion_sort,
    lambda a, b, c: heap_sort(heapify(a), b, c),
    quick_sort
])
def test_sort(f):
    for _ in range(10):
        A = [-1] + [random.randint(0, 1000) for _ in range(50)]
        B = sorted(A)
        f(A, 0, len(A) - 1)
        assert A == B

        C = [-1, 54, 88, 77, 26, 93, 17, 49, 10, 17, 77, 11, 31, 22, 44, 17, 20]
        D = [-1, 10, 11, 17, 17, 17, 20, 22, 26, 31, 44, 49, 54, 77, 77, 88, 93]
        f(C, 0, len(C) - 1)
        assert C == D
