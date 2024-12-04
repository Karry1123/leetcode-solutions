from typing import List
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        p = l1  # p指向l1链表
        q = l2  # q指向l2链表
        carry = 0  # 初始化进位为0
        newhead = ListNode()  # 新链表的虚拟头节点
        cur = newhead  # cur指向当前操作的链表节点

        while p or q:  # 遍历两个链表，直到p和q都为空
            val1 = p.val if p else 0  # 获取p节点的值，若p为空则为0
            val2 = q.val if q else 0  # 获取q节点的值，若q为空则为0
            sum_val = val1 + val2 + carry  # 计算当前位的和
            carry = sum_val // 10  # 更新进位
            cur.next = ListNode(sum_val % 10)  # 将当前位的结果存入新节点
            cur = cur.next  # cur指向新创建的节点

            if p: p = p.next  # 如果p不为空，指向p的下一个节点
            if q: q = q.next  # 如果q不为空，指向q的下一个节点

        if carry:  # 如果最后有进位，创建新的节点
            cur.next = ListNode(carry)

        return newhead.next  # 返回新链表的头节点