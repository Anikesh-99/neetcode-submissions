class Solution:
    def canJump(self, nums: List[int]) -> bool:
        reach = 0
        for i, num in enumerate(nums):
            if reach < i: return False
            reach = max(reach, num + i)
            
        return reach >= len(nums) - 1