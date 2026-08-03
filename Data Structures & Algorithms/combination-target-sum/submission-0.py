class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        st = set()
        n = len(nums)
        nums.sort()
        def backtrack(currIdx, lst, sm):
            if sm == target:
                st.add(tuple(lst))
                return
            if sm > target:
                return
            for i in range(currIdx, n):
                if target - nums[i] < 0: break
                backtrack(i, lst + [nums[i]], sm + nums[i])
        backtrack(0, [], 0)
        return [list(x) for x in list(st)]