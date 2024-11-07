# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = prev = ListNode(val=-inf, next=head)
        sorted_node, cur, head.next = head, head.next, None
        while cur:
            next, prev, sorted_node = cur.next, dummy, dummy.next
            while sorted_node and cur.val > sorted_node.val:
                prev, sorted_node = sorted_node, sorted_node.next
            prev.next, cur.next, cur = cur, sorted_node, next
        return dummy.next


        
        