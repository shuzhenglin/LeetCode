# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # 双指针
        f, r = head ,head
        for i in range(n):
            # 特殊情况：一开始n=1,r.next=NULL
            if r.next:
                r = r.next
            else:
                return head.next
        while r.next:
            f = f.next
            r = r.next
        f.next = f.next.next # 删去f指向的后一个节点，即倒数第n个节点
        return head