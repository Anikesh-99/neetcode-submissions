class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        left, right = 1, 1
        ans = [0] * n
        for i in range(len(nums)):
            if i == 0:
                ans[i] = left
            else:
                left *= nums[i - 1]
                ans[i] = left
        for i in range(n - 1, -1, -1):
            if i == n - 1:
                ans[i] *= right
            else:
                right *= nums[i + 1]
                ans[i] *= right
        return ans
