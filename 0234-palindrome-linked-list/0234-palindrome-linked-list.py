# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        prev = ListNode(next=head)
        slow = fast = head
        while fast and fast.next:
            prev, slow, fast = prev.next, slow.next, fast.next.next
        prev.next = None
        prev = None
        
        while slow:
            next = slow.next
            slow.next = prev
            prev, slow = slow, next

        while prev and head and prev.val == head.val:
            prev, head = prev.next, head.next
        return not prev or not head
        


        