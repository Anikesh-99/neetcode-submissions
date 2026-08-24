class Solution:
    def minWindow(self, s: str, t: str) -> str:
        def testdict(target, curr):
            for key in target:
                if key not in curr or target[key] > curr[key]:
                    return False
            return True
        target = Counter(t)
        l = 0
        size = len(s) + 1
        ans = ""
        curr = {}
        have, need = 0, len(target)
        while l < len(s) and s[l] not in target:
            l += 1
        for r in range(l, len(s)):
            if s[r] not in target: continue
            curr[s[r]] = curr.get(s[r], 0) + 1
            if curr[s[r]] == target[s[r]]: have += 1
            while have == need:
                if size > r - l + 1:
                    size = r - l + 1
                    ans = s[l: r + 1]
                curr[s[l]] -= 1
                if s[l] in target and curr[s[l]] < target[s[l]]: have -= 1
                l += 1 
                while l < r and s[l] not in target: l += 1
        return ans