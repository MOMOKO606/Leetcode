# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        prev, ans = None, -inf
        slow = fast = head
        while fast:
            fast = fast.next.next
            slow_next = slow.next
            slow.next = prev
            prev, slow = slow, slow_next
        h1, h2 = prev, slow
        while h1 and h2:
            ans = max(ans, h1.val + h2.val)
            h1, h2 = h1.next, h2.next
        return ans