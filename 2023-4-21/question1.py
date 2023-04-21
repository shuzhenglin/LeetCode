# Definition for singly-linked list.
# from typing import Optional
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: list[Optional[ListNode]]) -> Optional[ListNode]:
        import heapq
        heap = []
        # 构建小根堆
        for l in lists:
            while l:
                heapq.heappush(heap, l.val) # 加入链表的所有元素
                l = l.next
        res = ListNode(0)
        p = res
        while heap:
            p.next = ListNode(heapq.heappop(heap)) # 每次取堆顶节点
            p = p.next
        return res.next