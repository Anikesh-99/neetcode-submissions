class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        ans = 0
        for i in range(len(heights)):
            curr = heights[i]
            currArea = heights[i]
            for j in range(i + 1, len(heights)):
                curr = min(heights[j], curr)
                currArea = max(currArea, curr * (j - i + 1))
            ans = max(currArea, ans)
        return ans
