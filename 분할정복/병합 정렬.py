def merge_sort(A, left, right, merge_func):
    if left < right:
        mid = (left + right) // 2
        merge_sort(A, left, mid, merge_func)
        merge_sort(A, mid + 1, right, merge_func)
        merge_func(A, left, mid, right)

def merge(A, left, mid, right):
    L = A[left:mid+1]
    R = A[mid+1:right+1]
    l, r = 0, 0
    i = left
    
    while l < len(L) and r < len(R):
        if L[l] < R[r]:
            A[i] = L[l]
            l += 1
        else:
            A[i] = R[r]
            r += 1
        i += 1
            
    while l < len(L):
        A[i] = L[l]
        i += 1
        l += 1
        
    while r < len(R):
        A[i] = R[r]
        i += 1
        r += 1

def merge_class(A, left, mid, right):
    i, j, k = left, mid + 1, left
    sorted = [0] * (right + 1)
    
    while i <= mid and j <= right:
        if A[i] <= A[j]:
            sorted[k] = A[i]
            i += 1
        else:
            sorted[k] = A[j]
            j += 1
        k += 1
    
    if i > mid:
        sorted[k:k + (right + 1 - j)] = A[j:right + 1]
    else:
        sorted[k:k + (mid + 1 - i)] = A[i:mid + 1]
        
    A[left:right + 1] = sorted[left:right + 1]
        
import random
from copy import deepcopy
l = 20
A = [random.randint(0, l) for _ in range(l)]
B = deepcopy(A)

print(A)
merge_sort(A, 0, len(A) - 1, merge)
print(A)
merge_sort(B, 0, len(B) - 1, merge_class)
print(B)