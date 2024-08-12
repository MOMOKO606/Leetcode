# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = prev = ListNode(101)
        cur = head
        while cur:
            while prev and cur and cur.val == prev.val:
                cur = cur.next
            prev.next = cur
            prev = cur
            if cur: cur = cur.next
        return dummy.next
        