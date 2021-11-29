## LeetCode:  Reverse Integer
## https://leetcode.com/problems/reverse-integer/
class Solution:
    def reverse(self, x: int) -> int:
        
        sym = True if x>=0 else False
        x = abs(x)
        rev = 0
        while x>0:
            rev = rev*10 + x%10
            x = x//10
        
        rnge = [-2147483648, 2147483647] 
        
        if rev<=rnge[1] and rev>=rnge[0]:
            if sym==True:
                return rev
            else:
                return 0-rev
        else:
            return 0
