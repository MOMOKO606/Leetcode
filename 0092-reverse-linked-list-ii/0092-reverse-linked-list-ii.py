# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        def reverseFromNode(cur, count):
            tail, prev = cur, None
            while count != right:
                count += 1
                next = cur.next
                cur.next = prev
                prev, cur = cur, next
            tail.next = cur
            return prev
        
        dummy = prev = ListNode(next=head)
        cur, count = head, 0
        while cur:
            count += 1
            if count == left:
                newHead = reverseFromNode(cur, count - 1)
                prev.next = newHead
                return dummy.next
            prev, cur = cur, cur.next
        return dummy.next
        