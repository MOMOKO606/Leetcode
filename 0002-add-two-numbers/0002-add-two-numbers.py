# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = prev = ListNode()
        carry = 0
        while l1 or l2 or carry:
            if l1: carry, l1 = carry + l1.val, l1.next
            if l2: carry, l2 = carry + l2.val, l2.next
            cur = ListNode(val=carry % 10)
            prev.next, prev = cur, cur
            carry //= 10
        return dummy.next
        