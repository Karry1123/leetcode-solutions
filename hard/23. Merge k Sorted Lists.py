from typing import List
from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def merge2Lists(self, l1, l2):
        head=point=ListNode(0)
        while l1 and l2:
            if l1.val<=l2.val:
                point.next=l1
                l1=l1.next
            else:
                point.next=l2
                l2=l2.next
            point=point.next
        if l1:
            point.next=l1
        else:
            point.next=l2
        return head.next
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        amount=len(lists)
        interval=1
        while amount>interval:
            for i in range(0,amount-interval,2*interval):
                lists[i]=self.merge2Lists(lists[i], lists[i+interval])
            interval*=2
        return lists[0] if amount>0 else None