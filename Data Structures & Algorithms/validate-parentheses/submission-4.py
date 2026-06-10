class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in range(len(s)):
            if s[i] in "({[":
                stack.append(s[i])
                continue
            if s[i] == ")" and (not stack or stack.pop() != "("): return False
            if s[i] == "}" and (not stack or stack.pop() != "{"): return False
            if s[i] == "]" and (not stack or stack.pop() != "["): return False
            
        return len(stack) == 0