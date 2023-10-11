# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = prev = slow = fast = ListNode(next = head)
        while fast:
            fast = fast.next.next if fast.next else fast.next
            slow, prev = slow.next, slow
        prev.next = slow.next
        return dummy.next
