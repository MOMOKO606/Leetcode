# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = dummy = ListNode(next=head)
        slow = fast = head
        while fast and fast.next:
            fast = fast.next.next if fast.next else None
            prev, slow = slow, slow.next
        prev.next = slow.next
        return dummy.next
        