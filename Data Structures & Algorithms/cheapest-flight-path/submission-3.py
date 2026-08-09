class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj = defaultdict(list)
        for start, end, price in flights:
            adj[start].append((price, end))
        if src not in adj: return -1
        queue = deque(map(lambda x: (0, x[0], x[1]), adj[src]))
        visited = set()
        finalPrice = float('inf')
        memo = {}
        while queue:
            # print(queue)
            hop, price, dest = queue.popleft()
            if hop > k: break
            if dest in memo and memo[dest] <= price: continue 
            if dest == dst: finalPrice = min(price, finalPrice); continue
            if dest not in adj: continue
            memo[dest] = price
            newLocs = adj[dest]
            for contPrice, newLoc in newLocs:
                queue.append((hop + 1, contPrice + price, newLoc))
        return finalPrice if finalPrice != float('inf') else -1
