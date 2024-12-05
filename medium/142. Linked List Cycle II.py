from typing import Optional
from typing import List
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        seen = set()  # 用来存储访问过的节点
        while head:
            if head in seen:  # 如果节点已经访问过，说明有环
                return head
            seen.add(head)  # 将当前节点加入集合
            head = head.next  # 移动到下一个节点
        return None  # 如果遍历结束都没有环，返回 None