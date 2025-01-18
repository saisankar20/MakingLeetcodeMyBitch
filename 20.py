class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        matching_brackets = {'(': ')', '[': ']', '{': '}'}

        for char in s:
            if char in matching_brackets:
                stack.append(char)
            else:
                if stack and matching_brackets[stack[-1]] == char:
                    stack.pop()
                else:
                    return False

        return len(stack) == 0
