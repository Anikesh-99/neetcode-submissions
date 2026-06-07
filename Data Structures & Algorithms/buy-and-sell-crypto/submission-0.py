class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left, right = [1e9] * len(prices), [0] * len(prices)
        left[0] = prices[0]
        right[-1] = prices[-1]
        ans = 0
        for i in range(1, len(prices)):
            left[i] = min(left[i - 1], prices[i])
        for i in range(len(prices) - 2, -1, -1):
            right[i] = max(right[i + 1], prices[i])
        for i in range(len(prices)):
            ans = max(ans, right[i] - left[i])
        return ans
