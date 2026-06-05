class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hm = defaultdict(int)
        for i in range(len(nums)):
            hm[nums[i]] = 0
        visited = set()
        def dfs(n):
            if n in visited: return hm[n]
            visited.add(n)
            if n + 1 in visited: 
                hm[n] += (hm[n + 1] + 1)
                return hm[n]
            if n + 1 not in hm: 
                hm[n] = 1
                return 1
            hm[n + 1] += dfs(n + 1)    
            hm[n] += (hm[n + 1] + 1)
            return hm[n]
        ans = 0
        for i in nums:
            ans = max(dfs(i), ans)
        return ans