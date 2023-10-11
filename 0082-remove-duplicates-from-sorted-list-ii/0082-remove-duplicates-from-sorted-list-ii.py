# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = dummy = ListNode(next = head)
        cur = head
        while cur:
            next = cur.next
            while next and cur.val == next.val:
                cur, next = cur.next, next.next
            if prev.next != cur:
                cur = next
                prev.next = cur
            else:
                prev, cur = cur, next
        return dummy.next
        