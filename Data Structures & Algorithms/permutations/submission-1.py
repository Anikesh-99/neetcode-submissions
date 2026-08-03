class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans, path = [], []
        n = len(nums)
        used = [False] * len(nums)
        def backtrack():
            if len(path) == n: 
                ans.append(path[:])
                return
            for i in range(n):
                if used[i]: continue
                used[i] = True
                path.append(nums[i])
                backtrack()
                path.pop()
                used[i] = False
        backtrack()
        return ans