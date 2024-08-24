# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        dummy = prev = ListNode()
        while carry or l1 or l2:
            if l1: carry, l1 = carry + l1.val, l1.next
            if l2: carry, l2 = carry + l2.val, l2.next
            cur = ListNode(carry % 10)
            carry //= 10
            prev.next = cur
            prev = cur
        return dummy.next
