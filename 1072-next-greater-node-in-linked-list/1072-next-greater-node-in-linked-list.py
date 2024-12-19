# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        n, cur = 0, head
        while cur: cur, n = cur.next, n + 1

        ans, stack, i, cur = [0] * n, [], 0, head
        while cur:
            while stack and cur.val > stack[-1][1]:
                k, _ = stack.pop()
                ans[k] = cur.val
            stack.append([i, cur.val])
            cur, i = cur.next, i + 1
        return ans

        