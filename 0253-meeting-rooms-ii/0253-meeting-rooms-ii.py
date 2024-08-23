class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        min_heap, intervals, ans = [], sorted(intervals), 1
        for start, end in intervals:
            while min_heap and start >= min_heap[0]:
                heapq.heappop(min_heap)
            heapq.heappush(min_heap, end)
            ans = max(ans, len(min_heap))
        return ans


        