from typing import List
from typing import Optional
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=list()
        operater={
            "+",
            "-",
            "*",
            "/",
        }
        for i in range(len(tokens)):
            if tokens[i] in operater:
                a = int(stack.pop())
                b = int(stack.pop())
                if tokens[i] == "+":
                    c=a+b
                elif tokens[i]=="-":
                    c=b-a
                elif tokens[i]=="*":
                    c=a*b
                else:
                    c=b/a
                stack.append(int(c))
            else:
                stack.append(int(tokens[i]))
        return stack[-1]