from heapq import heappush, heappop

class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        i, maxHeap, minHeap, ans = -1, [], [], 0
        for j in range(len(nums)):
            heappush(maxHeap, (-nums[j], j))
            heappush(minHeap, (nums[j], j))
            while -maxHeap[0][0] - minHeap[0][0] > limit:
                i += 1
                while maxHeap[0][1] <= i:
                    heappop(maxHeap)
                while minHeap[0][1] <= i:
                    heappop(minHeap)
            ans = max(ans, j - i)
        return ans




        