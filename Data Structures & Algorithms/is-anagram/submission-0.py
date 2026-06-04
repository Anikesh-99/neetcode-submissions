class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
        count1, count2 = Counter(s), Counter(t)
        
        for key in count1:
            if key not in count2 or count2[key] != count1[key]: return False
        return True