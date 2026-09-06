class Solution:
    def canJump(self, nums: List[int]) -> bool:
        reach = 0
        for i, num in enumerate(nums):
            if i != 0 and reach < i: return False
            reach = max(i + nums[i], reach)
        return reach >= len(nums) - 1