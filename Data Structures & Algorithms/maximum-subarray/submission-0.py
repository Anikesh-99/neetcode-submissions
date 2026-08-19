class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        currSm = 0
        ans = max(nums)
        for num in nums:
            currSm += num
            ans = max(currSm, ans)
            if currSm < 0:
                currSm = 0
        return ans