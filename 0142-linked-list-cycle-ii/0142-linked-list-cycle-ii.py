# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head: return head
        slow = fast = head
        while True:
            slow = slow.next
            fast = fast.next.next if fast.next else None
            if not fast: return None
            if slow == fast: break

        slow = head
        while slow != fast:
            slow, fast = slow.next, fast.next
        return slow
        