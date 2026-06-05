class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        left, right = [1] * n, [1] * n
        left[0] = nums[0]
        right[-1] = nums[-1]
        for i in range(1, len(nums)):
            left[i] = left[i - 1] * nums[i]
        for i in range(len(nums) - 2, -1, -1):
            right[i] = right[i + 1] * nums[i]
        ans = [1] * n
        for i in range(n):
            if i == 0: ans[i] = right[i + 1]
            elif i == n - 1: ans[i] = left[i - 1]
            else: ans[i] = left[i - 1] * right[i + 1]
        return ans