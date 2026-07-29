class Solution:
    def numDecodings(self, s: str) -> int:
        dp = [0] * len(s)
        ref = set([str(i) for i in range(1, 27)])
        if len(s) == 1: return 0 if s[0] == '0' else 1
        if s[0] == '0': return 0
        dp[0] = 1
        if s[:2] in ref: dp[1] += 1
        if s[1] in ref: dp[1] += 1
        # print(dp)
        for i in range(2, len(dp)):
            if s[i] not in ref:
                dp[i] = 0
            else:
                dp[i] = dp[i - 1]
            if s[i - 1:i + 1] in ref:
                dp[i] += dp[i - 2]
            
        # print(dp)
        return dp[-1]