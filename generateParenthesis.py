## leetcode: Generate Parentheses
## https://leetcode.com/problems/container-with-most-water/

class Solution:
    def generateParenthesis(self, n: int):
        return genPar('(', 1, 1, n)

def genPar(x, cOpen, tOpen, n):
    if cOpen==0:
        if tOpen==n:
            return [x]
        else:
            return genPar(x+'(', cOpen+1, tOpen+1, n)
    if tOpen==n:
        return genPar(x+')', cOpen-1, tOpen, n)
    
    return genPar(x+'(', cOpen+1, tOpen+1, n) + genPar(x+')', cOpen-1, tOpen,n )
    
            
s = Solution()
inp = int(input())
print(s.generateParenthesis(inp))