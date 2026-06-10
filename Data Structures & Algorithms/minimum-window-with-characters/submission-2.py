class Solution:
    def minWindow(self, s: str, t: str) -> str:
        def testdict(target, curr):
            for key in target:
                if key not in curr or target[key] > curr[key]:
                    return False
            return True
        target = Counter(t)
        charsAchieved = 0
        l = 0
        while l < len(s):
            if s[l] in target: break
            l += 1
        ans, currLen = "", len(s) + 1
        curr = defaultdict(int)
        nxt = 0
        for r in range(l, len(s)):
            if s[r] not in target: continue
            curr[s[r]] += 1
            nxt = r
            # print(target, curr)
            while testdict(target, curr):
                print(s[l: r+ 1])
                if currLen > r - l + 1:
                    currLen = r - l + 1 
                    ans = s[l: r + 1]
                curr[s[l]] -= 1
                l += 1
                while l < r and s[l] not in target:
                    l += 1
        while testdict(target, curr):
            if currLen > nxt - l + 1:
                currLen = nxt - l + 1 
                ans = s[l: nxt + 1]
            curr[s[l]] -= 1
            l += 1
            while l < nxt and s[l] not in target:
                l += 1
        return ans