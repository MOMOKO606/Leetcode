# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        def splitList(node):
            prev = ListNode(next=node)
            slow = fast = node
            while fast and fast.next:
                prev, slow, fast = prev.next, slow.next, fast.next.next
            prev.next, next, slow.next = None, slow.next, None
            return [slow, node, next] if slow != node else [slow, None, next]

        if not head: return head
        root, left, right = splitList(head)
        return TreeNode(val=root.val, left=self.sortedListToBST(left), right=self.sortedListToBST(right))
            
        
        