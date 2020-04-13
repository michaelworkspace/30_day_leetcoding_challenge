"""
Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Example:

Input: [0,1,0,3,12]
Output: [1,3,12,0,0]
Note:

You must do this in-place without making a copy of the array.
Minimize the total number of operations.
"""


from typing import List



class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # non_zeros = []
        # for num in nums:
        #     if num != 0:
        #         non_zeros.append(num)
        # non_zeros += [0] * nums.count(0)
        # return non_zeros
        
        i = 0
        for x in range(len(nums)):
            if nums[x] != 0:
                nums[i], nums[x] = nums[x], nums[i]
                i += 1
