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
        if not head: return 
        prev = ListNode(next=head)
        slow = fast = head
        while fast and fast.next and fast.next.next:
            prev, slow, fast = slow, slow.next, fast.next.next
        
        prev.next = None
        left = self.sortedListToBST(head) if slow != head else None
        right = self.sortedListToBST(slow.next)
        return TreeNode(val=slow.val, left=left, right=right)
        