# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(next=head) # 构造一个哨兵节点用于反转一个k链
        p = dummy 
        pre = None # 构造pre节点，使节点由pre->cur->nxt,变为pre<-cur<-nxt
        cur = head
        n = 0
        while cur:
            n += 1
            cur = cur.next # 计算链表长度，用于判断需要反转多少次k链
        cur = head # 复位cur
        while n >= k:
            n -= k
            for _ in range(k): # 执行k次next的反转,得到新的k链
                nxt = cur.next
                cur.next = pre
                pre = cur
                cur = nxt
            # 对k链整体进行翻转
            nxt = p.next # 需要移动p作为新的k链边界，翻转后的新的边界会是p.next，故在翻转前存下p.next
            p.next.next = cur
            p.next = pre
            p = nxt
        return dummy.next