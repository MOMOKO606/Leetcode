# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def get_length(node):
            count = 0
            while node:
                node, count = node.next, count + 1
            return count

        
        if not head: return head
        k %= get_length(head)
        if not k: return head
        
        slow = fast = head
        while k:
            fast, k = fast.next, k - 1
        while fast.next:
            slow, fast = slow.next, fast.next
        newHead, slow.next = slow.next, None
        fast.next = head
        return newHead
        

        