class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        hm = defaultdict(list)
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i == j: continue
                hm[nums[i] + nums[j]].append([i, j])
        st = set()
        for i in range(len(nums)):
            if -nums[i] not in hm: continue
            for x, y in hm[-nums[i]]:
                if x == i or y == i: continue
                st.add(tuple(sorted([nums[x], nums[y], nums[i]])))
        return list(st)