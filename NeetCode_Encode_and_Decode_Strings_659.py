# Design an algorithm to encode a list of strings to a string. The encoded string 
# is then sent over the network and is decoded back to the original list of strings.


# Input: ["lint","code","love","you"]
# Output: ["lint","code","love","you"]
# Explanation:
# One possible encode method is: "lint:;code:;love:;you"

# Input: ["we", "say", ":", "yes"]
# Output: ["we", "say", ":", "yes"]
# Explanation:
# One possible encode method is: "we:;say:;:::;yes"

class Solution:
    # def encode(self, strs):
    #     new_srt = ''
    #     for s in strs:
    #         # new_srt += str(len(s)) + "#" + s
    #         new_srt += f"{len(s)}#{s}"

    #     return new_srt
    

    # def decode(self, str):
    #     i=0
    #     new_length = 0
    #     arr = []
    #     while i < len(str):
    #         if str[i] == "#":
    #             new_length = int(str[i-1])
    #             # print(str[i+1: i+1+new_length])
    #             arr.append(str[i+1: i+1+new_length])
    #             i += new_length+1
    #         i+=1
    #         # print(i)

    #     return arr
    
    # ======= NeetCode ==========
    def encode(self, strs):
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res
    
    def decode(self, s):
        res, i = [], 0

        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            res.append(s[j + 1 : j + 1 + length])
            i = j + 1 + length
        return res
    
solution_ins = Solution()

# print(solution_ins.encode(["lint","code","love","you"]))
print(solution_ins.decode("4#lint4#code4#love3#you"))
# solution_ins.decode("5#li#nt4#code4#love3#you")

