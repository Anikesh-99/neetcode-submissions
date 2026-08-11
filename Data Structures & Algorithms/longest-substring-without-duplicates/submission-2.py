class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        unique = set()
        l, r, mx = 0, 0, 0
        for r in range(len(s)):
            if s[r] not in unique:
                mx = max(mx, r - l + 1)
            else:
                while s[r] in unique:
                    unique.remove(s[l])
                    l += 1
            unique.add(s[r])
        return mx