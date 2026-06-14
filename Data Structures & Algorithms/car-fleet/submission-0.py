class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        combined = sorted(zip(position, speed), reverse=True)
        idx = 0
        ans = 0
        while idx < len(combined):
            time = (target - combined[idx][0])/combined[idx][1]
            # print(stack, time)
            if not stack: 
                stack.append(time)
                ans += 1
            elif stack[0] < time:
                stack.pop()
                stack.append(time)
                ans += 1
            idx += 1
        return ans
