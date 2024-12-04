from typing import Optional  # 导入 Optional 类型
#Definition for singly-linked list.
class ListNode:
	def __init__(self, x):
		self.val = x
		self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        countA = 0
        countB = 0
        tempA = ListNode
        tempB = ListNode
        tempA,tempB = headA,headB
        while tempA:
            countA+=1
            tempA=tempA.next
        while tempB:
            countB+=1
            tempB=tempB.next
        tempA,tempB = headA,headB
        if countA>=countB:
            sub=countA-countB
            while sub > 0:
                tempA=tempA.next
                sub-=1
        else:
            sub=countB-countA
            while sub > 0:
                tempB=tempB.next
                sub-=1
        while tempA!=tempB:
            tempA=tempA.next
            tempB=tempB.next
            if not tempA or not tempB:
                return None
        return tempA
        