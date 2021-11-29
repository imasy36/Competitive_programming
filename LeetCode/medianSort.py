## https://leetcode.com/problems/median-of-two-sorted-arrays/submissions/

class Solution:
    
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        arr = self.merge(nums1, nums2)
        if len(arr)%2==0:
            return (arr[len(arr)//2]+arr[len(arr)//2 -1])/2
        return arr[len(arr)//2]
    
    def merge(self, arr1, arr2):
        
        res = []
        i=0
        j=0
        
        while i<len(arr1) and j<len(arr2):
            if arr1[i]<arr2[j]:
                res.append(arr1[i])
                i+=1
            else:
                res.append(arr2[j])
                j+=1
        
        while i<len(arr1):
            res.append(arr1[i])
            i+=1
        
        while j<len(arr2):
            res.append(arr2[j])
            j+=1
        
        return res

