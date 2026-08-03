class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        st = set()
        n = len(nums)
        nums.sort()
        def backtrack(currIdx, lst):
            st.add(tuple(lst))
            if currIdx == n: 
                return
            for i in range(currIdx, n):
                backtrack(i + 1, lst + [nums[i]])
        backtrack(0, [])
        return [list(x) for x in list(st)]
