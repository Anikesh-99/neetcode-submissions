class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2): return False
        need = Counter(s1)
        curr = Counter(s2[:len(s1)])
        for i in range(len(s1), len(s2)):
            if need == curr: return True
            curr[s2[i - len(s1)]] -= 1
            if curr[s2[i - len(s1)]] == 0: del(curr[s2[i - len(s1)]])
            curr[s2[i]] += 1
        return need == curr