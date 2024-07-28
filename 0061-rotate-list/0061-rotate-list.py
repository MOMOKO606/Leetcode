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
        
        n = get_length(head)
        if not n: return head
        k %= n
        if not k: return head

        slow, fast, steps = head, head, k
        while steps:
            fast = fast.next
            steps -= 1
        while fast.next:
            slow, fast = slow.next, fast.next
        
        new_head = slow.next
        slow.next = None
        fast.next = head
        
        return new_head
        