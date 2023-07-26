from typing import List
# Given an unsorted array of integers nums, return the length of 
# the longest consecutive elements sequence.
# You must write an algorithm that runs in O(n) time.

# Example
# Input: nums = [100,4,200,1,3,2]
# Output: 4
# Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.

# class Solution:
#     def longestConsecutive(self, nums: List[int]) -> int:
#         return 3



nums = [0,3,7,2,5,8,4,6,0,1]
print(nums)
nums.sort()
print(nums)

nums = [0,3,7,2,5,8,4,6,0,1]
sorted_nums = sorted(nums, key=lambda num: num, reverse=False)
print(sorted_nums)


# Input: nums = [0,3,7,2,5,8,4,6,0,1]
# Output: 9