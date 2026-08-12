class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        ans = [0] * n
        stack = []
        for i, temp in enumerate(temperatures):
            while stack and stack[-1][0] < temp:
                tmp, idx = stack.pop()
                ans[idx] = (i - idx)
            stack.append((temp, i))
        return ans