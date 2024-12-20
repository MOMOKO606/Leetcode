# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = dummy = ListNode(next=head)
        preSums, cur, preSum = {0: prev}, head, 0
        while cur:
            preSum += cur.val
            preSums[preSum] = cur
            cur = cur.next
        
        preSum = 0
        while prev:
            preSum += prev.val
            prev.next = preSums[preSum].next
            prev = prev.next
        return dummy.next

        