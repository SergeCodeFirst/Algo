class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        my_set = set()

        l=0

        for r in s:
            while r in my_set:
                my_set.remove(s[l])
                l += 1
                
            my_set.add(r)
            longest = max(longest, len(my_set))
        
        return longest