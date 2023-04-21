# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        res = ListNode(next = head) # 设置边界节点
        pre = res # pre为移动指针
        while pre.next and pre.next.next: # 要求移动指针的下个和下下个节点都有元素才能交换
            left = pre.next # left始终位于移动指针右边一位
            right = left.next # right始终位于left指针右边一位
            left.next = right.next
            right.next = left # 交换操作
            pre.next = right # 移动指针复位
            pre = pre.next.next # 移动指针一次移动2位
        return res.next