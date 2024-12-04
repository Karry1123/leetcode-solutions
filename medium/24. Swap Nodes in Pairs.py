from typing import List
from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        temp = ListNode
        N1 = head
        N2 = head.next        
        head = N2
        while True:
            temp.next = N2.next
            N1.next = temp.next
            N2.next = N1

            if not temp.next or not temp.next.next :
                break
            N2 = temp.next.next
            N1.next = N2
            N1 = temp.next
        return head