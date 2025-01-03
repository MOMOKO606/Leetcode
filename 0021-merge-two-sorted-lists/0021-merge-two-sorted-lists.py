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
                cur, list1 = list1, list1.next
            else:
                cur, list2 = list2, list2.next
            prev.next = cur
            prev = cur
        prev.next = (list1 or list2)
        return dummy.next

        