"""
Given a non-empty array of integers, every element appears twice except for one. Find that single one.

Note:

Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

Example 1:

Input: [2,2,1]
Output: 1
Example 2:

Input: [4,1,2,1,2]
Output: 4
"""


from typing import List


class Solution:
    # Python solution
    def singleNumber(self, nums: List[int]) -> int:
        for num in nums:
            if nums.count(num) == 1:
                return num


    # Cool solution with Bitwise XOR
    def bitwise_singleNumber(self, nums: List[int]) -> int:
        res = 0
        for num in nums:
            res ^= num
        return res

    
S = Solution()
assert(S.singleNumber([1,2,2,3,1]) == 3)
assert(S.bitwise_singleNumber([1,2,2,3,1]) == 3)
