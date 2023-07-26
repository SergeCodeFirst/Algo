from typing import List
from collections import defaultdict
# Given an array of strings strs, group the anagrams together. You can return the answer in any order.
# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, 
# typically using all the original letters exactly once.


# Example
# Input: strs = ["eat","tea","tan","ate","nat","bat"]
# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

# Input: strs = [""]
# Output: [[""]]

# Input: strs = ["a"]
# Output: [["a"]]

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:# SOLUTION 1
        res = defaultdict(list) # key:combiantion of a char and it count - value: array of string with simillar char combination

        for s in strs:
            count = [0] * 26 # a .... z

            for c in s:
                count[ord(c) - ord("a")] += 1

            res[tuple(count)].append(s)
        return res.values()



    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        dic_list = defaultdict(list)

        for s in strs:
            position = [0]*26 # a .... z

            for c in s:
                position[ord(c) - ord("a")] += 1

            dic_list[tuple(position)].append(s)
        # print(dic_list)
        # print(dic_list.keys())
        # print(dic_list.values())
        return dic_list.values()

# print(groupAnagrams(["eat","tea","tan","ate","nat","bat"]))

new_solution = Solution()

print(new_solution.groupAnagrams(["eat","tea","tan","ate","nat","bat"]))
print(new_solution.groupAnagrams([""]))
print(new_solution.groupAnagrams(["a"]))


# #  EXPLANATION # SOLUTION 1
# arr = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", 't', "u", "v", "w", "x", "y", "z"]
# arr = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] # default number

# # getting the index 
# arr[ord("e") - ord("a")] += 1 #index of "e" ( arr[ord("e") - ord("a")] ) and we increment the zero at that index
# arr[ord("a") - ord("a")] += 1 #index of "e"
# arr[ord("c") - ord("a")] += 1 #index of "e"

# # Getting world combination base on an array. 
# # We increment by one when we land on an index that conrespond to the letter on the default arr 
# # we use the same index on the second arr to find the zero to increment.
# arr = [1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] # eac
# arr = [1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] # ace

# # turn the array inti tupple . both (eac, ace) have a specific unique key that let us know the are anagram
# tuple = (1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0) # eac
# tuple = (1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0) # ace 


# # Add the recent combination tupple as a key and make its value to be an array of string that match the key (AKA anagrames)
# {
#     (1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0) : ["eac", "ace"]
# }

# # Now we just return the value of each key
