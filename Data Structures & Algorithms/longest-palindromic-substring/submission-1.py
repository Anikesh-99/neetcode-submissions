class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) <= 1: return s
        longestStr = ""
        def isPalindrome(i, j):
            ln = 0
            if i == j:
                ln = 1
            while i >= 0 and j < len(s) and s[i] == s[j]:
                ln += 2
                i -= 1
                j += 1
            return s[i + 1: j] if ln != 0 else ""
        for i in range(len(s) - 1):
            s1 = isPalindrome(i, i)
            s1 = s[i] if not s1 else s1
            s2 = isPalindrome(i, i + 1)
            if len(s1) > len(longestStr):
                longestStr = s1
            if len(s2) > len(longestStr):
                longestStr = s2
        return longestStr