from typing import List

# Given an integer array nums and an integer k, 
# return the k most frequent elements. You may return the answer in any order.

# Input: nums = [1,1,1,2,2,3], k = 2
# Output: [1,2]

# Input: nums = [1], k = 1
# Output: [1]

class Solution:
    # def topKFrequent(self, nums: List[int], k: int) -> List[int]:
    #     # create a map num - count
    #     num_Count = {}
    #     res = []

    #     # Populate the map
    #     for num in nums:
    #         num_Count[num] = num_Count.get(num, 0) + 1
        
    #     # Sorting the map base of the count value of each key.
    #     sortedMap = sorted(num_Count.items(), key=lambda item: item[1], reverse=True)

    #     # get the most k frequent element
    #     for key, val in sortedMap:
    #         if len(res) == k:
    #             break
    #         res.append(key)
    #     return res
    
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # create map
        new_Map = {}
        res = []

        freq1 = [[] for i in range(len(nums) + 1)] # list comprehension create multiple distinct instance of list (when one is updated, it does not automaticaly update the other)
        # In this case, you're correctly creating a list of distinct empty lists using a list comprehension. 
        # Each inner list is a separate object, so appending elements to one inner list doesn't affect the others.
        
        # freq2 = [[]] * (len(nums) + 1) # create multiple unique instance of list (when one is updated, it automaticaly update the other)
        # # you're creating a list of empty lists, but all of these inner lists are the same object. 
        # # So, when you append an element to one of these inner lists, the change is reflected in all of them
        
        for num in nums:
            new_Map[num] = new_Map.get(num, 0) + 1

        for key, val in new_Map.items():
            freq1[val].append(key)
            # freq2[val].append(key)
        # print(freq2)

        for i in range(len(freq1) - 1, 0, -1):
            for num in freq1[i]:
                if len(res) == k:
                    break
                res.append(num)
        
        return res
    
NewSolution = Solution()
print(NewSolution.topKFrequent([1,1,1,2,2,3], 2))

# QUESTION
# when i create freq like this 
# freq1 = [[]] * (len(nums) + 1)
# it looks like this [[], [], [], [], [], [], []]
# the same thing goes for 
# freq2 = [[] for i in range(len(nums) + 1)]
# it looks like this [[], [], [], [], [], [], []]

# for key, val in new_Map.items():
#     freq1[val].append(key)
#     freq2[val].append(key)

# freq1 looks like :[[1, 2, 3], [1, 2, 3], [1, 2, 3], [1, 2, 3], [1, 2, 3], [1, 2, 3], [1, 2, 3]]
# and freq2 look like: [[], [3], [2], [1], [], [], []]
# Why?