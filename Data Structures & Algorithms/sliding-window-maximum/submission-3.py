class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if len(nums) <= k: return [max(nums)]
        currMax = -10001
        ans = []
        hm = defaultdict(int)
        for i in range(k):
            hm[nums[k]] += 1
            currMax = max(currMax, nums[i])
        ans.append(currMax)
        for i in range(k, len(nums)):
            prevln = len(hm)
            hm[nums[i - k]] -= 1
            if hm[nums[i - k]] <= 0: del(hm[nums[i-k]])
            # print(prevln, len(hm), hm)
            if currMax <= nums[i]: currMax = nums[i]
            elif currMax not in hm:
                # print(currMax, nums[i - k], nums[i]) 
                currMax = max(nums[i - k + 1: i + 1])
            hm[nums[i]] += 1
            ans.append(currMax)
        return ans