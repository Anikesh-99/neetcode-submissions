class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        n = len(candidates)
        res = []
        def backtrack(startIdx, lst, left):
            if left == 0: res.append(lst.copy()); return
            for i in range(startIdx, n):
                if i > startIdx and candidates[i] == candidates[i - 1]:
                    continue
                if candidates[i] > left: break
                lst.append(candidates[i])
                backtrack(i + 1, lst, left - candidates[i])
                lst.pop()
        backtrack(0, [], target)
        return res