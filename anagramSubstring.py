## interviewbit: https://www.interviewbit.com/problems/anagram-match/

class Solution:
    # @param A : string
    # @param B : list of strings
    # @return a list of integers
    def solve(self, A, B):
        lA = len(A)
        count = [0 for i in range(len(B))]
        for x in range(len(B)):
            lB = len(B[x])
            for j in range(0,lA-lB+1):
                if self.chckAna(B[x], A[j:j+lB]):
                    count[x]+=1
        return count
        
    def chckAna(self, s1, s2):
        count = [0 for x in range(256)]
        i = 0
        for i in range(len(s1)):
            count[ord(s1[i])-ord('a')]+=1
            count[ord(s2[i])-ord('a')]-=1
        for i in range(256):
            if count[i]!=0:
                return False
        return True

s = Solution()
inp1 = input()
inp2 = input().split()
print(s.solve(inp1, inp2))