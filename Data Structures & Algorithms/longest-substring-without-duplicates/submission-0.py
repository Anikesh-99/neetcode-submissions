class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        unique = set()
        l, r = 0, 0
        mx = 0
        i = 0
        while r < len(s):
            if s[r] not in unique:
                unique.add(s[r])
                mx = max(mx, len(unique))
            else:
                while s[r] in unique:
                    unique.remove(s[l])
                    l += 1
                unique.add(s[r])
            r += 1
        return mx
                    