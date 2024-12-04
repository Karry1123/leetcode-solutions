from typing import Optional  # 导入 Optional 类型
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        while head:
            if head.val == val:
                head = head.next
            else:
                break
        newhead = head
        last = head
        if head:
            head = head.next
        else:
            return newhead
        while head:
            if head.val == val:
                last.next = head.next
                head = head.next
            else:
                last = last.next
                head = head.next
        return newhead
        