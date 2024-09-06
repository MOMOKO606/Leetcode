# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = fast = head
        while slow and fast:
            slow = slow.next
            fast = fast.next.next if fast.next else None
            if slow and fast and slow == fast: break
        else:
            return None

        fast = head
        while slow != fast:
            slow, fast = slow.next, fast.next
        return slow
        