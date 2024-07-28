# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        prev = dummy = ListNode(next = head)
        cur, count = head, 0
        while cur:
            cur, count, prev = cur.next, count + 1, cur
        if count < 2: return head
        tail = prev

        k, prev, cur = k % count, dummy, head
        if not k: return head
        
        target = count - k
        while target:
            cur, prev = cur.next, cur
            target -= 1
        prev.next, newHead = None, cur

        tail.next = head
        return newHead