from typing import Optional  # 导入 Optional 类型
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        newhead = ListNode()
        p = list1
        q = list2
        if p and q:
            if p.val<q.val:
                newhead.val=p.val
                p = p.next
            else:
                newhead.val=q.val
                q = q.next
        elif p:
            return list1
        else:
            return list2
        r = newhead
        while p and q:
            if p.val<q.val:
                r.next = p
                p = p.next
                r = r.next
            else:
                r.next = q
                q = q.next
                r = r.next
        if p:
            r.next = p
        else:
            r.next = q
        return newhead