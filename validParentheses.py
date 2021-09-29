## LeetCode: Valid Parentheses
## https://leetcode.com/problems/valid-parentheses/

class Solution:
    def opp(self, curr, nxt):
        if curr == '(' and nxt==')':
            return True
        if curr == '[' and nxt==']':
            return True
        elif curr == '{' and nxt=='}':
            return True
        else:
            return False
        
    def isValid(self, s: str) -> bool:
        stack = []
        for x in s:
            if x in ['(', '[', '{']:
                stack.append(x)
            else:
                if len(stack)<1 or self.opp(stack[-1],x)==False:
                    return False
                stack.pop()
        if len(stack)!=0:
            return False
        return True