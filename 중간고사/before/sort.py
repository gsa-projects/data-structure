import pytest
import random

#%% Selection Sort
def selection_sort(A, low, high):
    for i in range(len(A)):     # TODO: len(A) - 1. 틀린 건 아님
        min_idx = i

        for j in range(i + 1, len(A)):  # TODO: i + 1 -> i. 틀린 건 아님
            if A[j] < A[min_idx]:
                min_idx = j

        A[min_idx], A[i] = A[i], A[min_idx]
#%% Insertion Sort
def insertion_sort(A, low, high):
    for i in range(1, len(A)):
        for j in range(i, 0, -1):   # TODO: 여기부터 다 틀림
            if A[j - 1] > A[j]:
                A[j - 1], A[j] = A[j], A[j - 1]
#%% Heap Sort
def downheap(H, i, size):
    while 2*i <= size:  # 자식이 존재할 때
        max_child = 2*i     # 최대 힙 만들기
        if 2*i < size:  # 2*i + 1 <= size, 즉 오른쪽 자식도 존재할 때
            if H[2*i + 1] > H[max_child]:
                max_child = 2*i + 1

        if H[i] >= H[max_child]:    # 이거 맞냐?
            break

        H[i], H[max_child] = H[max_child], H[i]
        i = max_child   # max_child가 root가 되어 다시 얘의 자식에 대해 downheap 적용하는 루프

def heapify(A):
    size = len(A) - 1   # 힙 트리 인덱스는 1부터 시작하니까
    for i in range(size // 2, 0, -1):   # 마지막 자식의 root부터 최상위 노드까지
        downheap(A, i, size)    # 최대 힙 성질 유지하도록 힙 트리 재구조화

    return A

def heap_sort(A, low, high):
    size = len(A) - 1
    for _ in range(size):   # 노드 교환 -> 다운 힙 한 번에 마지막 값이 하나씩 정렬 완료되므로 크기가 1씩 감소함 -> size 번 반복
        A[1], A[size] = A[size], A[1]   # 최상위 노드와 최하위 노드 교환 -> 맨 마지막은 정렬 완료
        size -= 1   # 맨 마지막 정렬 완료되었으므로 크기 1 감소
        downheap(A, 1, size)
#%% Quick Sort
def quick_sort(A, left, right):
    if left < right:
        p = partition(A, left, right)
        quick_sort(A, left, p - 1)
        quick_sort(A, p + 1, right)

def partition(A, left, right):
    pivot = A[left]:
        while low <= right and A[low] <= pivot:
            low += 1
        while left <= high and pivot < A[high]:
            high -= 1

        if low < high:
            A[low], A[high] = A[high], A[low]

    A[left], A[high] = A[high], A[left]
    return high
#%%

# @pytest.mark.parametrize("f", [
#     selection_sort,
#     insertion_sort,
#     lambda a, b, c: heap_sort(heapify(a), b, c),
#     quick_sort
# ])
# def test_sort(f):
#     for _ in range(10):
#         A = [-1] + [random.randint(0, 1000) for _ in range(50)]
#         B = sorted(A)
#         f(A, 0, len(A) - 1)
#         assert A == B

A = [54, 88, 77, 26, 93, 17, 49, 10, 17, 77, 11, 31, 22, 44, 17, 20]
print(A)
quick_sort(A, 0, len(A) - 1)
print(A)