class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) <= 1: return s
        def helper(l, r):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            return [l + 1, r - 1]
        ans = s[0]
        for i in range(len(s) - 1):
            l1, r1 = helper(i - 1, i + 1)
            l2, r2 = helper(i, i + 1)
            if r1 - l1 + 1 > len(ans):
                ans = s[l1: r1 + 1]
            if r2 - l2 + 1 > len(ans):
                ans = s[l2: r2 + 1]
        return ans