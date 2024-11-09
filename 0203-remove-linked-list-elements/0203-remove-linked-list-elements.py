# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummy = prev = ListNode(next=head)
        cur = head
        while cur:
            next = cur.next
            if cur.val == val:
                prev.next = next
            else:
                prev = cur
            cur = next 
        return dummy.next
        