# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        dummy = prev = ListNode(next=head) 
        deque, cur = collections.deque(), head
        while cur:
            deque.append(cur)
            cur = cur.next
        
        while deque:
            node = deque.popleft()
            node.next = None
            prev.next = node
            prev = node
            if deque:
                node = deque.pop()
                node.next = None
                prev.next = node
                prev = node
        return dummy.next
                


        