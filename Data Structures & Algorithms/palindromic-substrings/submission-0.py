class Solution:
    def countSubstrings(self, s: str) -> int:
        count = 0
        def generate(x, y):
            nonlocal count
            while x >= 0 and y < len(s) and s[x] == s[y]:
                count += 1
                x -= 1
                y += 1
        for i in range(len(s) - 1):
            generate(i, i)
            generate(i, i + 1)
        return count + 1