from typing import List
from typing import Optional
class MyCircularDeque:

    def __init__(self, k: int):
        self.stack1=[]
        self.stack2=[]
        self.k=k

    def insertFront(self, value: int) -> bool:
        if len( self.stack1)+len(self.stack2)<self.k:
            self.stack1.append(value)
            return True
        else:
            return False

    def insertLast(self, value: int) -> bool:
        if len(self.stack1)+len(self.stack2)<self.k:
            self.stack2.append(value)
            return True
        else:
            return False

    def deleteFront(self) -> bool:
        if self.stack1:
            self.stack1.pop()
            return True
        elif not self.stack1 and not self.stack2:
            return False
        else:
            while self.stack2:
                self.stack1.append(self.stack2.pop())
            self.stack1.pop()
            return True

    def deleteLast(self) -> bool:
        if self.stack2:
            self.stack2.pop()
            return True
        elif not self.stack1 and not self.stack2:
            return False
        else:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
            self.stack2.pop()
            return True

    def getFront(self) -> int:
        if self.stack1:
            return self.stack1[-1]
        elif not self.stack1 and not self.stack2:
            return -1
        else:
            while self.stack2:
                self.stack1.append(self.stack2.pop())
            return self.stack1[-1]

    def getRear(self) -> int:
        if self.stack2:
            return self.stack2[-1]
        elif not self.stack1 and not self.stack2:
            return -1
        else:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
            return self.stack2[-1]

    def isEmpty(self) -> bool:
        if not self.stack1 and not self.stack2:
            return True
        else:
            return False

    def isFull(self) -> bool:
        if len(self.stack1)+len(self.stack2)==self.k:
            return True
        else:
            return False


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()