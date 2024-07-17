# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = prev = ListNode()
        while list1 and list2:
            if list1.val <= list2.val:
                cur, list1 = ListNode(list1.val), list1.next
            else:
                cur, list2 = ListNode(list2.val), list2.next
            prev.next = cur
            prev = prev.next
        prev.next = list1 or list2
        return dummy.next
        
        