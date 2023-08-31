from typing import List
# Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].
# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
# You must write an algorithm that runs in O(n) time and without using the division operation.

# Input: nums = [1,2,3,4]
# Input: nums = [1,2,3,4]
# Output: [24,12,8,6]


# Input: nums = [-1,1,0,-3,3]
# Output: [0,0,9,0,0]

class Solution:
    # def productExceptSelf(self, nums: List[int]) -> List[int]:
    #     result_num = []
    #     for i in range(len(nums)):
    #         temp_num = 1
    #         for j in range(len(nums)):
    #             if i == j:
    #                 continue
    #             temp_num = nums[j] * temp_num
    #         result_num.append(temp_num)
    #     return result_num

    # def productExceptSelf(self, nums: List[int]) -> List[int]:
    #     ans = [1] * len(nums)
    #     leftProd = [1] * len(nums)
    #     rightProd = [1] * len(nums)

    #     leftProduct = 1
    #     for n in nums:
    #         leftProd[i] = leftProduct
    #         leftProduct *= n

    #     rightProduct = 1
    #     for i in range(len(nums) - 1, -1, -1):
    #         rightProd[i] = rightProduct
    #         rightProduct *= n

    #     for i in range(len(nums)):
    #         ans[i] = leftProd[i] * rightProd[i]

    #     return ans
    
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)
        
        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]
        
            postfix = 1
        for i in range(len(nums) -1, -1, -1):
            res[i]  *= postfix
            postfix *= nums[i] 

        return res




solution = Solution()
print(solution.productExceptSelf([1,2,3,4])) #[24,12,8,6]
# print(solution.productExceptSelf([-1,1,0,-3,3])) #[0,0,9,0,0]
