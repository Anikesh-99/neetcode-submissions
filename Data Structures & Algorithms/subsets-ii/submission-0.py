class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        st = set()
        n = len(nums)
        nums.sort()
        def backtrack(idx, lst):
            if idx == n: 
                return
            st.add(tuple(lst))
            for i in range(idx + 1, n):
                backtrack(i, lst + [nums[i]])
        backtrack(-1, [])
        return [list(tup) for tup in st]