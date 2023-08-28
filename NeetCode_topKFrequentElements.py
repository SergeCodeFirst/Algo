from typing import List
from collections import defaultdict

# Given an integer array nums and an integer k, 
# return the k most frequent elements. You may return the answer in any order.

# Input: nums = [1,1,1,2,2,3], k = 2
# Output: [1,2]

# Input: nums = [1], k = 1
# Output: [1]

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for i in range(len(nums) + 1)]
        
        # freq = []
        # for i in range(len(nums) + 1):
        #     freq.append([])

        for n in nums:
            count[n] = 1 + count.get(n, 0)
        for n, c in count.items():
            freq[c].append(n)

        res = []
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res

    # def topKFrequent(self, nums: List[int], k: int) -> List[int]:
    #     # Create hasmap make a key from the integer in the array
    #     newMap = defaultdict(int)
    #     res =[]
    #     # Increment everytime you get on a key
    #     for num in nums:
    #         newMap[num] += 1
        
    #     # Sort the keys based on their frequency in descending order
    #     allKeys = sorted(newMap.keys(), key=lambda x: newMap[x], reverse=True)

    #     for key in allKeys:
    #         if len(res) == k:
    #             break
    #         res.append(key)
    #     return res
    


newSolution = Solution()
print(newSolution.topKFrequent([1,1,1,2,2,3], 2))
# print(newSolution.topKFrequent([1], 1))