class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        if len(s) % 2 != 0: return False
        mapping = {"(": ")", "{": "}", "[":"]"}
        for i, c in enumerate(s):
            if c in "({[": 
                stack.append(c)
                continue
            if not stack: return False
            curr = stack.pop()
            if mapping[curr] != c: return False
        return len(stack) == 0