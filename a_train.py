
from typing import List
from collections import defaultdict

# Given an array of strings strs, group the anagrams together. You can return 
# the answer in any order. An Anagram is a word or phrase formed by rearranging 
# the letters of a different word or phrase, typically using all the original 
# letters exactly once.

# Example :
# Input: strs = ["eat","tea","tan","ate","nat","bat"]
# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

# Input: strs = [""]
# Output: [[""]]

# Input: strs = ["a"]
# Output: [["a"]]

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # create a defaultdict(List)
        my_dict = defaultdict(list)
        res = []

        # iterate trought strs and sort the srting to create a key
        for s in strs:
            sort_srt = ''.join(sorted(s))
            # if the current sorted string match the key, we add it
            my_dict[sort_srt].append(s)
        
        # we return defaultdicti values 
        for k,v in my_dict.items():
            res.append(v)
        
        return res
        # return my_dict.values()
    
    # def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
    #     my_dict = defaultdict(list)

    #     for s in strs:
    #         my_arr = [0]*26 # a ----> z
            
    #         for c in s:
    #             my_arr[ord(c) - ord("a")] +=1
            
    #         my_dict[tuple(my_arr)].append(s)
        
    #     return my_dict.values()

new_solution = Solution()

print(new_solution.groupAnagrams(["eat","tea","tan","ate","nat","bat"]))
print(new_solution.groupAnagrams([""]))
print(new_solution.groupAnagrams(["a"]))