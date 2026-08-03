class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        n = len(nums)
        def backtrack(lst):
            if len(lst) == n: 
                ans.append(lst)
                return
            for num in nums:
                if num in lst: continue
                backtrack(lst + [num])
        backtrack([])
        return ans