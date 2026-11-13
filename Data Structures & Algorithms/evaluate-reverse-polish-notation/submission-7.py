class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        num =[]
        operator = set(["+","-","*","/"])
        result =0
        for i in range(len(tokens)):
            if tokens[i] not in operator:
                num.append(int(tokens[i]))
            else:
                a= num.pop()
                b= num.pop()
                if tokens[i]=="+":
                   num.append(a + b)
                elif tokens[i]=="-":
                     num.append(b-a)
                elif tokens[i]=="*":
                    num.append(a*b)
                else:
                    num.append(int(b/a))
        
        return num[-1]