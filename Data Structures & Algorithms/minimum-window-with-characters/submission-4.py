class Solution:
    def minWindow(self, s: str, t: str) -> str:
        def testdict(target, curr):
            for key in target:
                if key not in curr or target[key] > curr[key]:
                    return False
            return True
        target = Counter(t)
        l = 0
        while l < len(s):
            if s[l] in target: break
            l += 1
        ans, currLen = "", len(s) + 1
        curr = defaultdict(int)
        for r in range(l, len(s)):
            if s[r] not in target: continue
            curr[s[r]] += 1
            nxt = r
            while testdict(target, curr):
                if currLen > r - l + 1:
                    currLen = r - l + 1 
                    ans = s[l: r + 1]
                curr[s[l]] -= 1
                l += 1
                while l < r and s[l] not in target:
                    l += 1
        return ans