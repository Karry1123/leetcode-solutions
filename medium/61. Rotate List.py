from typing import Optional
from typing import List
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return head
        lastnode=head
        l=1
        while lastnode.next!=None:
            l+=1
            lastnode=lastnode.next
        remains=l-k%l
        breaknode=head
        if remains==0:
            return head
        while remains>1:
            breaknode=breaknode.next
            remains-=1
        lastnode.next=head
        head=breaknode.next
        breaknode.next=None
        return head