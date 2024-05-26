from heapq import heapify as Heapify, heappush, heappop
from copy import deepcopy

def downheap2(A, i, size):
    while (k := 2*i) <= size:
        if k < size and A[k] < A[k + 1]:
            k += 1
        if A[k] <= A[i]:
            break

        A[i], A[k] = A[k], A[i]
        i = k

# 최대 힙
def create_heap(A):
    hsize = len(A) - 1
    for i in reversed(range(1, hsize//2 + 1)):
        downheap2(A, i, hsize)

def heap_sort2(A):
    n = len(A) - 1
    for i in range(n):
        A[1], A[n] = A[n], A[1]
        downheap(A, 1, n - 1)
        n -= 1
#
# A = [-1, 54, 88, 77, 26, 93, 17, 49, 10, 17, 77, 11, 31, 22, 44, 17, 20]
# # print(A)
# create_heap(A)
# print(A)
# heap_sort(A)
# print(A)

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

A = [54, 88, 77, 26, 93, 17, 49, 10, 17, 77, 11, 31, 22, 44, 17, 20]
print('A', [-1] + A)

f = lambda a, b, c: heap_sort(heapify([-1] + a), b, c)
print(sorted([-1] + A))
f(A, 0, 0)
print(A)

# C = deepcopy(A)
# create_heap(C)
# heap_sort2(C)
# print('C', C)
#
# D = deepcopy(A)
# heapify(D)
# heap_sort(D, 0, 0)
# print('D', D)
