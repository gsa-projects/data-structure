def dfs(grid, i, j):
        #땅이 아닌 경우 종료
        if i<0 or i>=len(grid) or j<0 or j>=len(grid[0]) or grid[i][j]!='1':
            return
        
        grid[i][j]=0

        #동서남북 탐색
        dfs(grid, i+1, j)
        dfs(grid, i-1, j)
        dfs(grid, i, j+1)
        dfs(grid, i, j-1)

def numIslands(grid):
    cnt = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == '1':
                dfs(grid, i, j)
                #모든 육지 탐색 후 cnt 1 증가
                cnt += 1
    return cnt           

print(numIslands([
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]))