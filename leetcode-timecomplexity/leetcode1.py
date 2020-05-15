# Given a sorted array nums, remove the duplicates in-place such that each element appear only once and return the new length.

class Solution:
    def removeDuplicates(self, nums):
        i = 0
        while i < len(nums)-1:
            if nums[i] == nums[i+1]:
                del nums[i]
            else:
                i += 1
        return len(nums)
    
#The time complexity of this would be O(n) because it is directly proportional to the size of the input.
