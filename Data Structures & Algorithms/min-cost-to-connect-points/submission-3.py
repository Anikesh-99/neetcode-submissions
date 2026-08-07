class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        adj = {i: [] for i in range(n)}
        for i, (x1, y1) in enumerate(points):
            for j in range(i + 1, n):
                x2, y2 = points[j]
                dist = abs(x2 - x1) + abs(y2 - y1)
                adj[i].append([dist, j])
                adj[j].append([dist, i])
        res = 0
        visited = set()
        minH = [[0, 0]]
        while len(visited) < n:
            cost, i = heapq.heappop(minH)
            if i in visited: continue
            res += cost
            visited.add(i)
            for neicost, nei in adj[i]:
                if nei not in visited:
                    heapq.heappush(minH, [neicost, nei])
        return res