class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [1] * n
        pref, suff = 1, 1
        for i, num in enumerate(nums):
            ans[i] = pref
            pref *= num
        for i in range(n - 1, -1, -1):
            ans[i] *= suff
            suff *= nums[i]
        return ans