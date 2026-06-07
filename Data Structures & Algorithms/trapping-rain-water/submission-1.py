class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        leftMax, rightMax = height[l], height[r]
        currVol = 0
        while l < r:
            if leftMax < rightMax:
                currVol += (leftMax - height[l])
                l += 1
                leftMax = max(height[l], leftMax)
            else:
                currVol += (rightMax - height[r])
                r -= 1
                rightMax = max(height[r], rightMax)
        return currVol
                