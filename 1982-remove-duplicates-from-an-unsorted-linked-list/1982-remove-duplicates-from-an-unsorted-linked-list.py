# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicatesUnsorted(self, head: ListNode) -> ListNode:
        freqs, cur, avoid = collections.defaultdict(int), head, set()
        while cur: freqs[cur.val], cur = freqs[cur.val] + 1, cur.next
        for val, freq in freqs.items(): 
            if freq > 1: avoid.add(val) 
        dummy = prev = ListNode(next=cur)
        cur = head
        while cur:
            if cur.val not in avoid: prev.next, prev = cur, cur
            cur = cur.next
        prev.next = cur
        return dummy.next

        