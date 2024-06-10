from collections import deque

def bfs(grid: list[list[int]], now: tuple[int, int], visited):
    m = len(grid)
    n = len(grid[0])
    
    visited[now[0]][now[1]] = True
    q = deque([now])
    
    while q:
        i, j = q.pop()
        
        ways = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        for di, dj in ways:
            if 0 <= i + di < m and 0 <= j + dj < n:
                if not visited[i + di][j + dj]:
                    if grid[i + di][j + dj] == '1':
                        q.append((i + di, j + dj))
                        visited[i + di][j + dj] = True

def dfs(grid: list[list[int]], now: tuple[int, int], visited):
    m = len(grid)
    n = len(grid[0])
    i, j = now
    visited[i][j] = True
    
    ways = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    for di, dj in ways:
        if 0 <= i + di < m and 0 <= j + dj < n:
            if not visited[i + di][j + dj]:
                if grid[i + di][j + dj] == '1':
                    dfs(grid, (i + di, j + dj), visited)

def dfs_teacher(grid: list[list[int]], i: int, j: int):
    if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] != "1":
        return
    
    grid[i][j] = 0
    dfs_teacher(grid, i + 1, j)
    dfs_teacher(grid, i - 1, j)
    dfs_teacher(grid, i, j + 1)
    dfs_teacher(grid, i, j - 1)

grid = [["1","1","0","0","0"],["1","1","0","0","0"],["0","0","1","0","0"],["0","0","0","1","1"]]
m = len(grid)
n = len(grid[0])

def me():
    cnt = 0
    visited = [[False] * n for _ in range(m)]
    for i in range(m):
        for j in range(n):
            if not visited[i][j]:
                if grid[i][j] == '1':   
                    # bfs(grid, (i, j), visited)
                    dfs(grid, (i, j), visited)
                    cnt += 1
    print(cnt)

def teacher():
    cnt = 0
    for i in range(m):
        for j in range(n):
            if grid[i][j] == '1':   
                dfs_teacher(grid, i, j)
                cnt += 1
    print(cnt)

teacher()