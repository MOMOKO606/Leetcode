# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # Build min heap
        minHeap = []
        for i, l in enumerate(lists):
            if l: heapq.heappush(minHeap, (l.val, i))

        dummy = prev = ListNode()
        while minHeap:
            val, i = heapq.heappop(minHeap)
            cur = ListNode(val=val)
            prev.next, lists[i], prev = cur, lists[i].next, cur
            if lists[i]: heapq.heappush(minHeap, (lists[i].val, i))
        return dummy.next
        