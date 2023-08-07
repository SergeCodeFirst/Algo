from typing import List
from collections import defaultdict

# Given an integer array nums and an integer k, return the k most frequent elements. 
# You may return the answer in any order.


# Input: nums = [1,1,1,2,2,3], k = 2
# Output: [1,2]

# Input: nums = [1], k = 1
# Output: [1]



class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        new_map = defaultdict(int)
        res = []
        
        for num in nums:
            new_map[num] += 1

        # print(new_map)
        sort_map = dict(sorted(new_map.items(), key=lambda item: item[1], reverse=True))

        # print(sort_map.items())
        for key, val in sort_map.items():
            if len(res) >= k:
                break

            res.append(key)
            # print(val)
        return res

solution_ins = Solution()

print(solution_ins.topKFrequent([2,1,1,1,2,3], k = 2))