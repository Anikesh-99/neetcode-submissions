class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        from bisect import bisect_left
        tails = []
        for num in nums:
            if not tails or num > tails[-1]:
                tails.append(num)
            else:
                idx = bisect_left(tails, num)
                tails[idx] = num
        return len(tails)