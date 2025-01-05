class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        min_heap, max_heap, ans, i = [], [], 0, -1
        for j, num in enumerate(nums):
            heapq.heappush(min_heap, (num, j))
            heapq.heappush(max_heap, (-num, j))
            while -max_heap[0][0] - min_heap[0][0] > limit:
                i += 1
                if i >= min_heap[0][1]: heapq.heappop(min_heap)
                if i >= max_heap[0][1]: heapq.heappop(max_heap)
            ans = max(ans, j - i)
        return ans
