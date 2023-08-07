# A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric 
# characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

# Given a string s, return true if it is a palindrome, or false otherwise.

# Example 1:
# Input: s = "A man, a plan, a canal: Panama"
# Output: true
# Explanation: "amanaplanacanalpanama" is a palindrome.

# Example 2:
# Input: s = "race a car"
# Output: false
# Explanation: "raceacar" is not a palindrome.

# Example 3:
# Input: s = " "
# Output: true
# Explanation: s is an empty string "" after removing non-alphanumeric characters.
# Since an empty string reads the same forward and backward, it is a palindrome.


class Solution:
    # def isPalindrome(self, s: str) -> bool:
    #     newStr = ''

    #     for c in s:
    #         if c.isalnum():
    #             newStr += c.lower()
        
    #     print(newStr)
    #     print(newStr[::-1])
        
    #     return newStr == newStr[::-1]

    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) -1

        while left < right:
            while left < right and not self.isAlphaNum(s[left]):
                left += 1
            
            while left < right and not self.isAlphaNum(s[right]):
                right -= 1

            if s[left].lower() != s[right].lower():
                return False
            
            left += 1
            right -= 1

        return True
    
    def isAlphaNum(self, c):
        return (
                ord("A") <= ord(c) <= ord("Z") or
                ord("a") <= ord(c) <= ord("z") or 
                ord("0") <= ord(c) <= ord("9")
                )

    
newSolution = Solution()

print(newSolution.isPalindrome("A man, a plan, a canal: Panama"))
print(newSolution.isPalindrome("race a car"))
print(newSolution.isPalindrome("0P"))