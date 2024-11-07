# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def merge(node1, node2):
            dummy = prev = ListNode()
            while node1 and node2:
                if node1.val < node2.val:
                    prev.next = node1
                    node1 = node1.next
                else:
                    prev.next = node2
                    node2 = node2.next
                prev = prev.next
            prev.next = (node1 or node2)
            return dummy.next

        def splitList(node):
            prev = ListNode(next=node)
            slow = fast = node
            while fast and fast.next:
                prev, slow, fast = prev.next, slow.next, fast.next.next
            prev.next = None
            return node, slow

        h1, h2 = splitList(head)
        if h1 == h2: return h1
        h1, h2 = self.sortList(h1), self.sortList(h2)
        return merge(h1, h2)
        