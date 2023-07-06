from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numToIndex = {}
        
        for i in range(len(nums)):
            numToIndex[nums[i]] = i
        
        for i in range(len(nums)):
            temp_val = target - nums[i]
            if(temp_val in numToIndex and numToIndex[temp_val] != i):
                return [i, numToIndex[temp_val]]
        return [0,0]
    
newSolution = Solution()
print(newSolution.twoSum([2,7,11,15], 9))