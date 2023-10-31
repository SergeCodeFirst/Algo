class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = set({ "+","-","*","/" })
        left =-1
        rigth =0
        mySum = 0

        while rigth < len(tokens):
            if tokens[rigth] not in operators:
                rigth +=1
                left +=1

            if tokens[rigth] == '+':
                mySum += tokens[left -1] + tokens[left]
            
            elif tokens[rigth] == '-':
                mySum += tokens[left -1] - tokens[left]

            elif tokens[rigth] == '*':
                mySum += tokens[left -1] * tokens[left]

            elif tokens[rigth] == '/':
                mySum += tokens[left -1] / tokens[left] 

        return mySum