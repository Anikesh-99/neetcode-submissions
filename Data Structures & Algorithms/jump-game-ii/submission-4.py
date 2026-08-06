class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) == 1: return 0
        reachable, jumps, theo = nums[0], 1, nums[0]
        for i in range(1, len(nums)):
            if theo >= len(nums) - 1: 
                return jumps + 1 if theo > reachable else jumps
            if i > reachable:
                reachable = theo
                jumps += 1
            theo = max(reachable, nums[i] + i)
            # print(reachable, theo, jumps)
        return jumps
            
