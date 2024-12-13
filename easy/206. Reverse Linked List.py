from typing import List
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #设计一个新listnode
        if not head:
            return None
        dummy=ListNode()
        dummy.next=head
        while head.next:
            tmp=head.next
            head.next=head.next.next
            tmp.next=dummy.next
            dummy.next=tmp
        return dummy.next