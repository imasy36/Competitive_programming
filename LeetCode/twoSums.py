## LeetCode: https://leetcode.com/problems/two-sum/submissions/
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums = [[nums[i],i] for i in range(len(nums))]
        nums.sort(key=lambda x:x[0])
        l=0
        h=len(nums)-1
        while l<h:
            if nums[l][0]+nums[h][0]==target:
                break
            elif nums[l][0]+nums[h][0]>target:
                h-=1
            else:
                l+=1
        return [nums[l][1],nums[h][1]]