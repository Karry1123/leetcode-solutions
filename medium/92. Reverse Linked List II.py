from typing import List
from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if left==right:
            return head
        newhead = ListNode()
        p=head
        q=head
        cur=newhead
        newhead.next=head
        if left==1:
            p = cur
        while right>0:
            if left==1:
                p = cur
            cur = cur.next
            left-=1
            right-=1
        q=cur
        while p.next !=q:
            temp = p.next
            p.next=temp.next
            temp.next=q.next
            q.next=temp
        return newhead.next