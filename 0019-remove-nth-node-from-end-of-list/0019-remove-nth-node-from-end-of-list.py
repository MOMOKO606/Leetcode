# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = prev = ListNode(next=head)
        slow = fast = head
        while fast and n:
            fast, n = fast.next, n - 1
        while fast:
            slow, fast, prev = slow.next, fast.next, prev.next
        prev.next = slow.next
        return dummy.next
        
        
        