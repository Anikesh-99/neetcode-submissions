class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = nums[0]
        pref, suff = 0, 0
        for i in range(len(nums)):
            pref = nums[i] * (pref or 1)
            suff = nums[len(nums) - 1 - i] * (suff or 1)
            res = max(res, max([pref, suff]))
        return res