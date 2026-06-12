class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        ans = [0] * len(temperatures)
        for i in range(len(temperatures)):
            while stack:
                # print(stack[-1][1], temperatures[i])
                if stack[-1][1] >= temperatures[i]: break
                idx, temp = stack.pop()
                ans[idx] = i - idx
            stack.append((i, temperatures[i]))
        return ans