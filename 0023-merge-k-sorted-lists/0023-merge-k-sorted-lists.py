# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        min_heap = []
        dummy = prev = ListNode()
        for i, node in enumerate(lists): 
            if node: heapq.heappush(min_heap, [node.val, i])
        
        while min_heap:
            _, i = heapq.heappop(min_heap)
            prev.next = lists[i]
            lists[i], prev = lists[i].next, prev.next
            if lists[i]:
                heapq.heappush(min_heap, [lists[i].val, i])
        return dummy.next

        