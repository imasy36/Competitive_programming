class Solution:
    def findMedianSortedArrays(self, nums1: list, nums2: list) -> float:
        res = mergeSort(nums1+nums2)
        if len(res)%2==0:
            ans = (res[len(res)//2] + res[len(res)//2 - 1 ]) / 2 
        else:
            ans = res[len(res)//2]
        return ans
    
def mergeSort(arr):
    if len(arr)==1:
        return arr
    mid = len(arr)//2
    l = mergeSort(arr[:mid])
    r = mergeSort(arr[mid:])
    
    return merge(l,r)

def merge(l,r):
    i,j = 0, 0
    arr = []
    
    while i<len(l) and j<len(r):
        if l[i]<r[j]:
            arr.append(l[i])
            i+=1
        else:
            arr.append(r[j])
            j+=1
    
    while i<len(l):
        arr.append(l[i])
        i+=1
    while j<len(r):
        arr.append(r[j])
        j+=1
    
    return arr

'''
Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.
Example :

    Input: nums1 = [1,3], nums2 = [2]
    Output: 2.00000
'''

s = Solution()
arr1 = [ int(x) for x in input("Enter Array1: ").split()]
arr2 = [ int(x) for x in input("Enter Array2: ").split()]
print("Median of the Sorted Array: " , s.findMedianSortedArrays(arr1, arr2))