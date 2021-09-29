## LeetCode: Median of Two Sorted Arrays
## https://leetcode.com/problems/median-of-two-sorted-arrays/

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
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
        
