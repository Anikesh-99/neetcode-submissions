class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        hm = defaultdict(int)
        l, r = 0, 0
        mx = 0
        res = 0
        for r in range(len(s)):
            hm[s[r]] = 1 + hm[s[r]]
            mx = max(mx, hm[s[r]])
            while (r - l + 1) - mx > k:
                hm[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1)
        return res