class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in range(len(s)):
            if s[i] == '(' or s[i] == '[' or s[i] == '{':
                stack.append(s[i])
            else:
                if not stack:
                    return False
                x = stack.pop()
                if s[i] == ')' and x != '(':
                    return False
                elif s[i] == ']' and x != '[':
                    return False
                elif s[i] == '}' and x != '{':
                    return False
        return not stack