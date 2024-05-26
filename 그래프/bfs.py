from queue import Queue

def bfs(vtx, alist, s):
    visited = [False] * len(vtx)
    queue = Queue()

    queue.put(s)
    visited[s] = True

    while not queue.empty():
        s = queue.get()
        print(vtx[s], end=' ')

        for v in alist[s]:
            if not visited[v]:
                queue.put(v)
                visited[v] = True

vtx = ['U', 'V', 'W', 'X', 'Y']
alist = [
    [1, 2],
    [0, 2, 3],
    [0, 1, 4],
    [1],
    [2]
]

print("bfs (start: U):", end=' ')
bfs(vtx, alist, 0)
