# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = prev = ListNode(next=head)
        fast = slow = head
        while fast and n:
            n, fast = n - 1, fast.next

        while fast:
            prev, slow, fast = slow, slow.next, fast.next

        prev.next = slow.next
        return dummy.next
        