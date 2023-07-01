from typing import List

# Given an integer array nums, return true if any value appears at least 
# twice in the array, and return false if every element is distinct.

# Input: nums = [1,2,3,1]
# Output: true

# Input: nums = [1,2,3,4]
# Output: false

# Input: nums = [1,1,1,3,3,4,3,2,4,2]
# Output: true

class Solution:
    # def containsDuplicate(self, nums: List[int]) -> bool:
    #     nums.sort()
    #     for i in range(len(nums)):
    #         if i == len(nums) -1:
    #             break
    #         if nums[i] == nums[i+1]:
    #             return True
    #     return False
    
    # def containsDuplicate(self, nums: List[int]) -> bool:
    #     map = {}
    #     for num in nums:
    #         map[num] = (map.get(num) or 0) + 1

    #     for k, v in map.items():
    #         if v > 1:
    #             return True
    #     return False
    
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashset = set()
        for num in nums:
            if num in hashset:
                return True
            hashset.add(num)
        return False



newSolution = Solution()
print(newSolution.containsDuplicate([1,2,3,4]))



