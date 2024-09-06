# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        queue, cur = deque([]), head
        while cur:
            queue.append(cur)
            cur = cur.next

        dummy = prev = ListNode()
        while queue:
            l = queue.popleft()
            r = queue.pop() if queue else None
            l.next = r
            if r: r.next = None
            prev.next = l
            prev = r
        return dummy.next

        