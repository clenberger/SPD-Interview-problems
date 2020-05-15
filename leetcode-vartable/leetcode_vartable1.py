#Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        for i in range(n):
            nums1[m] = nums2[i]
            m += 1
        nums1.sort()
        return nums1
    
# nums1 [1,2,3,4,5,6]
# m = 3
# nums2 [2,5,6]
# n = 3

#        nums1             nums2        m   n
#0  [1,2,3,4,5,6]        [2,5,6]        3   3
#1  
#2
#3