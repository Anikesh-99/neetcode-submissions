class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        def backtrack(counter, used, curr):
            if used == n:
                # print(curr)
                ans.append(curr + ")" * (2 * n - len(curr)))
                return
            # if curr == "(()": print(stack)
            if not counter:
                backtrack(counter + 1, used + 1, curr + "(")
                return
            backtrack(counter - 1, used, curr + ")")
            backtrack(counter + 1, used + 1, curr + "(")
        backtrack(0, 0, "")
        return ans
                