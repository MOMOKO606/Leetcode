# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        prev, cur = node, node.next
        while cur:
            prev.val = cur.val
            prev, cur = cur, cur.next


        prev, cur, next = node, node.next, node.next.next
        while next:
            prev, cur, next = cur, next, next.next
        prev.next = None
        