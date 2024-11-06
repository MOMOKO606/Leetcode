# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = fast = head
        while slow and fast:
            slow = slow.next
            fast = fast.next.next if fast.next else None
            if slow and fast and slow == fast: return True
        return False
        