class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [[0 for _ in range(len(coins))] for _ in range(amount + 1)]
        for i in range(len(coins)):
            dp[0][i] = 1
        coins.sort()
        for i in range(1, amount + 1):
            for j, coin in enumerate(coins):
                # print(coin, i, j, dp[i][j], dp[i][j - 1])
                dp[i][j] = dp[i][j - 1]
                if i >= coin: dp[i][j] += dp[i - coin][j]
            # print(dp)
        return dp[-1][-1] 