class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # ans = 0
        n = len(nums)
        memo = defaultdict()
        def helper(index, sm):
            # nonlocal ans
            if (index, sm) in memo: return memo[(index, sm)]
            if index == n and sm == target: return 1
            if index >= n: return 0
            memo[(index, sm)] = helper(index + 1, sm + nums[index]) + helper(index + 1, sm - nums[index])
            return memo[(index, sm)]
        return helper(0, 0)
        # return ans