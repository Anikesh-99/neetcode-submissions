class Solution:
    def longestPalindrome(self, s: str) -> str:
        def helper(i, j):
            while i >= 0 and j < len(s) and s[i] == s[j]:
                i -= 1
                j += 1
            return (i + 1, j)
        ans = ""
        for i in range(len(s)):
            i1, j1 = helper(i, i)
            i2, j2 = helper(i, i + 1)
            if j1 - i1 > len(ans): ans = s[i1: j1]
            if j2 - i2 > len(ans): ans = s[i2: j2]
        return ans