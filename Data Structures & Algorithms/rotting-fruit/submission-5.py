class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue = deque()
        visited = set()
        def isValid(x, y): return 0 <= x < len(grid) and 0 <= y < len(grid[0])
        dirs = [[-1, 0], [0, -1], [1, 0], [0, 1]]
        fresh = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2: 
                    queue.append((i, j, 0))
                    fresh += 1
                if grid[i][j] == 1: fresh += 1
        while queue:
            x, y, time = queue.popleft()
            visited.add((x, y))
            if len(visited) == fresh: return time
            for dirx, diry in dirs:
                newx, newy = x + dirx, y + diry
                if isValid(newx, newy) and (newx, newy) not in visited and grid[newx][newy] == 1:
                    queue.append((newx, newy, time + 1))
        return -1 if fresh else 0
