class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hm = {}
        for i in range(len(nums)):
            if target-nums[i] in hm: return [hm[target-nums[i]], i]
            if nums[i] not in hm: hm[nums[i]] = i
        return [-1, -1]