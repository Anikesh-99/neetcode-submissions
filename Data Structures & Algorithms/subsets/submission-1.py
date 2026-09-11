class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        ans = []
        subset = []
        def backtrack(i):
            if i >= n: ans.append(subset.copy()); return 
            subset.append(nums[i])
            backtrack(i + 1)
            subset.pop()
            backtrack(i + 1)
        backtrack(0)
        return ans
            