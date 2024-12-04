from typing import List
from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        newhead1 = ListNode()
        newhead2 = ListNode()
        p=newhead1
        q=newhead2
        cur=head
        count=1
        while cur:
            if count%2==1:
                p.next=cur
                p=p.next
            else:
                q.next=cur
                q=q.next
            cur=cur.next
            count+=1
        q.next=None
        p.next=newhead2.next
        return newhead1.next