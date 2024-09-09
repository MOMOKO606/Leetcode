# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def breakList(head):
            prev = ListNode(next=head)
            slow = fast = head
            while fast and fast.next:
                prev, slow, fast = slow, slow.next, fast.next.next
            prev.next = None
            return slow

        def merge(l1, l2):
            dummy = prev = ListNode()
            while l1 and l2:
                if l1.val <= l2.val:
                    prev.next = l1
                    l1 = l1.next
                else:
                    prev.next = l2
                    l2 = l2.next
                prev = prev.next
            prev.next = (l1 or l2)
            return dummy.next


        newHead = breakList(head)
        if head == newHead: return head
        return merge(self.sortList(head), self.sortList(newHead))
        
        