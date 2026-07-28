class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue = deque()
        numSpots = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2: 
                    queue.append((i, j, 0))
                if grid[i][j] != 0:
                    numSpots += 1
        dirs = [[-1, 0], [0, -1], [0, 1], [1, 0]]
        def isValid(x, y):
            return 0<= x < len(grid) and 0 <= y < len(grid[0])
        visited = set()
        timeTaken = 0
        while queue:
            x, y, mins = queue.popleft()
            if (x, y) in visited: continue
            timeTaken = max(mins, timeTaken)
            visited.add((x, y))
            for i, j in dirs:
                newx, newy = i + x, j + y
                if isValid(newx, newy) and grid[newx][newy] == 1:
                    queue.append((newx, newy, mins + 1))
        return timeTaken if numSpots == len(visited) else -1
        

