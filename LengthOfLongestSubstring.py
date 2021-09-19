# author: imasy36

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s)<1:
            return 0
        res = [ 1, s[0] ]
        for i in range(len(s)):
            for j in range(i+1,len(s)+1):
                temp = s[i:j]
                if len(set(list(temp)))==j-i:
                    if temp not in s[j:]:
                        if j-i>res[0]:
                            res[0] = j-i
                            res[1] = temp
                else:
                    break
        return res

'''
    Given a string s, find the length of the longest substring without repeating characters.
    Examlpe: 
        Input: s = "abcabcbb"
        Output: 3

'''
        
x = Solution()
inp = input("Enter a String: ")
print(x.lengthOfLongestSubstring(inp))