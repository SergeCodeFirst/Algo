# Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.
# In other words, return true if one of s1's permutations is the substring of s2.


# Example 1:
# Input: s1 = "ab", s2 = "eidbaooo"
# Output: true
# Explanation: s2 contains one permutation of s1 ("ba").

# Example 2:
# Input: s1 = "ab", s2 = "eidboaoo"
# Output: false


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool: 
        l=0
        srt_s1 = sorted(s1)
        
        for r in range(len(s2)):
            if s2[r] in s1:
                l = r
                r += len(s1)

                if srt_s1 == sorted(s2[l:r]):
                    return True
                
                else:
                    r -= r
                    l = r

        return False