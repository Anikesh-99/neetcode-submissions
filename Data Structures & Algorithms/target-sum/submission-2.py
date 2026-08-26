class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # ans = 0
        from functools import lru_cache
        n = len(nums)
        # memo = defaultdict()
        @lru_cache(None)
        def helper(index, sm):
            # nonlocal ans
            if index == n and sm == target: return 1
            if index >= n: return 0
            return helper(index + 1, sm + nums[index]) + helper(index + 1, sm - nums[index])
        return helper(0, 0)
        # return ans