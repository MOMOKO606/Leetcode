# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        odd = head
        even = head.next if head else None
        dummy1 = prev = ListNode(next=head)
        dummy2 = ListNode(next=even)
        while odd or even:
            if odd:
                odd.next = even.next if even else None
                prev, odd = odd, odd.next
            if even:
                even.next = even.next.next if even.next else None
                even =  even.next
        prev.next = dummy2.next
        return dummy1.next
        

        
        