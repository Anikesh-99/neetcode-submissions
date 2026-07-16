class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = [[False for _ in range(len(grid[0]))] for _ in range(len(grid))]
        dr = [[-1, 0], [0, -1], [1, 0], [0, 1]]
        def isValid(x, y):
            return 0 <= x < len(grid) and 0 <= y < len(grid[0])
        def dfs(x, y):
            visited[x][y] = True
            for i, j in dr:
                newx, newy = i + x, j + y
                if isValid(newx, newy) and not visited[newx][newy] and grid[newx][newy] == '1':
                    dfs(newx, newy)
        islands = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1' and not visited[i][j]:
                    dfs(i, j)
                    islands += 1
        return islands

        

