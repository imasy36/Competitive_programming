## LeetCode: Container With Most Water
## https://leetcode.com/problems/container-with-most-water/

class Solution:
    def maxArea(self, height: List[int]) -> int:
        mx = 0
        l = len(height)
        x=0
        y=l-1
        while x<y:
            area = (y-x)*min(height[x], height[y])
            if area>mx:
                mx = area
            if height[x]<height[y]:
                x+=1
            else:
                y-=1
        return mx
                