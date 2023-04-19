# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        l3 = ListNode()
        r = l3
        p = list1
        q = list2 # 引入双指针，分别指向两个列表
        while p and q:
            # 将较小的用尾插法插入l3
            if p.val <= q.val:
                r.next = p
                p = p.next
            else:
                r.next = q
                q = q.next
            r = r.next
        r.next = p if p else q # 将剩余链表直接插入l3
        return l3.next