from collections import deque


class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        ans, i, minQueue, maxQueue = 0, -1, deque([]), deque([])
        for j in range(len(nums)):
            while maxQueue and nums[j] > maxQueue[-1][0]:
                maxQueue.pop()
            maxQueue.append((nums[j], j))
            while minQueue and nums[j] < minQueue[-1][0]:
                minQueue.pop()
            minQueue.append((nums[j], j))
            while maxQueue[0][0] - minQueue[0][0] > limit:
                i += 1
                while maxQueue[0][1] <= i: maxQueue.popleft()
                while minQueue[0][1] <= i: minQueue.popleft()
            ans = max(ans, j - i)
        return ans



        