from heapq import heappush, heapify

class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        size = len(nums)
        heap_max = []
        heap_min = []

        ans = 0
        left, right = 0, 0
        while right < size:
            heapq.heappush(heap_max, [-nums[right], right])
            heapq.heappush(heap_min, [nums[right], right])

            while -heap_max[0][0] - heap_min[0][0] > limit:
                while heap_min[0][1] <= left:
                    heapq.heappop(heap_min)
                while heap_max[0][1] <= left:
                    heapq.heappop(heap_max)
                left += 1
            ans = max(ans, right - left + 1)
            right += 1

        return ans




        