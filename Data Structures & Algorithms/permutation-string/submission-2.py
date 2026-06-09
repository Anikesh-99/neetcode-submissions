class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2): return False
        l, r = 0, 0
        count = Counter(s1)
        while r < len(s2):
            if s2[r] in count:
                count[s2[r]] -= 1
                print(l, r, s2[r], count[s2[r]])
                
            while l < r and ((s2[r] in count and count[s2[r]] < 0) or (s2[r] not in count)):
                # print("Inside loop", l, r, count[s2[r]])
                if s2[l] in count: count[s2[l]] += 1
                l += 1
            if s2[r] not in count: l += 1
            # print(s2[l: r + 1], l ,r)
            if r - l + 1 == len(s1): 
                # print(s2[l: r+1])
                return True
            
            r += 1
        return False