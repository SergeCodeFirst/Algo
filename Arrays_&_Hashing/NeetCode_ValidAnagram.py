# Given two strings s and t, return true if t is an anagram of s, and false otherwise.

# An Anagram is a word or phrase formed by rearranging the letters of a different word 
# or phrase, typically using all the original letters exactly once.

# Input: s = "anagram", t = "nagaram"
# Output: true

# Input: s = "rat", t = "car"
# Output: false

class Solution:
    def isAnagram(self, s: str, t: str) -> bool: 
        temp_str = ""

        s = sorted(s)
        s = temp_str.join(s)

        t = sorted(t)
        t = temp_str.join(t)

        # if(s == t):
        #     return True
        # return False
        return s == t
    
    # def isAnagram(self, s: str, t: str) -> bool: 
    #     newMapS = {}
    #     newMapT = {}

    #     if len(s) != len(t):
    #         return False

    #     for char in s:
    #         newMapS[char] = (newMapS.get(char) or 0)+ 1
        
    #     for char in t:
    #         newMapT[char] = (newMapT.get(char) or 0)+ 1

    #     for char in s:
    #         if (char in newMapT):
    #             if newMapS.get(char) != newMapT.get(char):
    #                 return False
    #         else:
    #             return False

    #     return True


newSolution = Solution()

print(newSolution.isAnagram("a", "ab"))
# print(newSolution.isAnagram("anagram", "nagaram"))
# print(newSolution.isAnagram("rat", "cat"))