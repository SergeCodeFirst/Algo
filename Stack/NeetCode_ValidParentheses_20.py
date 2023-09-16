# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
# An input string is valid if:
# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.


# Example 1:
# Input: s = "()"
# Output: true

# Example 2:
# Input: s = "()[]{}"
# Output: true

# Example 3:
# Input: s = "(]"
# Output: false



class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in range(len(s)):
            if (s[i] == "(" or s[i] == "[" or s[i] == "{"):
                stack.append(s[i])
                continue

            if len(stack) == 0:
                return False
            
            if s[i] == ")" and stack[-1] != "(" or s[i] == "]" and stack[-1] != "[" or s[i] == "}" and stack[-1] != "{":
                return False
            
            stack.pop()

        if len(stack) > 0:
            return False

        return True
    
newSolution = Solution()
print(newSolution.isValid("(){}}{"))
# print(newSolution.isValid("()"))
print(newSolution.isValid("]"))