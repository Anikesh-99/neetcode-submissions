class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 1: return 1
        two, one = 1, 1
        curr = 0
        for i in range(2, n + 1):
            curr = two + one
            two = one
            one = curr
        return curr