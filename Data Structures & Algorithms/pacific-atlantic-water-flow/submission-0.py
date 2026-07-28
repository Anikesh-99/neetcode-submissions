class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        def isValid(x, y):
            return 0 <= x < len(heights) and 0 <= y < len(heights[0])
        dirs = [[0, -1], [-1, 0], [1, 0], [0, 1]]
        atl, pac = set(), set()
        def dfs(x, y, visit, prev):
            if (x, y) in visit or heights[x][y] < prev:
                return
            visit.add((x, y))
            for i, j in dirs:
                newx, newy = i + x, j + y
                if isValid(newx, newy):
                    dfs(newx, newy, visit, heights[x][y])
        for i in range(len(heights[0])):
            dfs(0, i, pac, heights[0][i])
            dfs(len(heights) - 1, i, atl, heights[-1][i])
        for i in range(len(heights)):
            dfs(i, 0, pac, heights[i][0])
            dfs(i, len(heights[0]) - 1, atl, heights[i][-1])
        res = []
        for i in range(len(heights)):
            for j in range(len(heights[0])):
                if (i, j) in atl and (i, j) in pac:
                    res.append((i, j))
        return res
            
        


