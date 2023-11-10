########### A bit slow ###########
from collections import deque

class Solution:
    def isValid(self, s: str) -> bool:
        stack = deque()
        for c in s:
            stack.append(c)

            if len(stack) > 1:
                if (stack[-2] == '(' and c == ')') or (stack[-2] == '{' and c == '}') or (stack[-2] == '[' and c == ']'):
                    stack.pop()
                    stack.pop()

        return len(stack)  == 0


########### A bit faster ###########
from collections import deque

# 3 ACTIONS: append, return False, pop

class Solution:
    def isValid(self, s: str) -> bool:
        stack = deque()
        for c in s:
            if c in "({[":
                stack.append(c)
            elif len(stack) == 0:
                return False # Do not continue
            elif stack[-1] == '(' and c != ')':
                return False # Do not continue
            elif stack[-1] == '{' and c != '}':
                return False # Do not continue
            elif stack[-1] == '[' and c != ']':
                return False # Do not continue
            else:
                stack.pop()

        return not stack
