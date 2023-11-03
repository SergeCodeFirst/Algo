# Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.
# There is only one repeated number in nums, return this repeated number.
# You must solve the problem without modifying the array nums and uses only constant extra space.



# Example 1:
# Input: nums = [1,3,4,2,2]
# Output: 2

# Example 2:
# Input: nums = [3,1,3,4,2]
# Output: 3

from typing import List

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        existing_num = set()
        for num in nums:
            if num in existing_num:
                return num
            existing_num.add(num)
        return -1
