class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = [[-1 for _ in range(n + 1)] for _ in range(n + 1)]
        for s, e, t in times:
            graph[s][e] = t
        queue = []
        for i, t in enumerate(graph[k]):
            if t != -1: queue.append((t, i))
        heapq.heapify(queue)
        visited = set([k])
        while queue:
            # print(queue)
            time, end = heapq.heappop(queue)
            if end in visited: continue
            visited.add(end)
            if len(visited) == n: return time
            for i, t in enumerate(graph[end]):
                if i not in visited and t != -1: heapq.heappush(queue, (t + time, i))
        return -1

