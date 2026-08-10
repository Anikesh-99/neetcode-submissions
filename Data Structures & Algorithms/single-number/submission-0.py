class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        x = nums[0]
        for num in nums[1:]:
            x = x ^ num
        return x
