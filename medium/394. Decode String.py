from typing import List
from typing import Optional
class Solution:
    def decodeString(self, s: str) -> str:
        stack = list()
        for char in s:
            if char != "]":
                stack.append(char)
            else:
                z = ""
                while stack and stack[-1]!="[":
                    z+=stack.pop()
                stack.pop()

                num = ""
                while stack and stack[-1].isdigit():
                    num+=stack.pop()
                num = int(num[::-1])

                new = z[::-1]*num
                for char in new:
                    stack.append(char)
        return "".join(stack)