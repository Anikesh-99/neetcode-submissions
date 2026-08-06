class Solution:
    def jump(self, nums: List[int]) -> int:
        reachable, jumps, theo = 0, 0, 0
        for i in range(len(nums) - 1):
            theo = max(theo, nums[i] + i)
            if i == reachable:
                reachable = theo
                jumps += 1
            # print(reachable, theo, jumps)
            
        return jumps
            
