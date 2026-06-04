class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hm = {}
        for i in range(len(strs)):
            s = "".join(sorted([j for j in strs[i]]))
            if s in hm:
                hm[s].append(strs[i])
            else:
                hm[s] = [strs[i]]
        return list(hm.values())