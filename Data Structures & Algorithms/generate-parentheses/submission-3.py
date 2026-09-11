class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        def backtrack(curr, opened, closed):
            if len(curr) == 2 * n: 
                ans.append(curr)
                return
            if opened < n: backtrack(curr + "(", opened + 1, closed)
            if closed < opened: backtrack(curr + ")", opened, closed + 1)
        backtrack("", 0, 0)
        return ans