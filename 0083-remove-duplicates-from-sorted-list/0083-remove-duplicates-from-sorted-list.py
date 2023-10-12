# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = prev = ListNode(val = math.inf, next = head)
        cur = head
        while cur:
            while cur and prev.val == cur.val:
                cur = cur.next
            prev.next = cur
            prev = cur
            if cur: cur = cur.next
        return dummy.next