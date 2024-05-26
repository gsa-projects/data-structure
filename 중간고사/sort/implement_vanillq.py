from heapq import heapify, heappush, heappop

A = [-1, 54, 88, 77, 26, 93, 17, 49, 10, 17, 77, 11, 31, 22, 44, 17, 20]
print(A)
# 최소 힙
heapify(A)
print(A)

S = []
while A:
    S.append(heappop(A))
print(S)