class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        minHeap, intervals, ans = [], sorted(intervals), -inf
        for interval in intervals:
            while minHeap and interval[0] >= minHeap[0]:
                heapq.heappop(minHeap)
            heapq.heappush(minHeap, interval[1])
            ans = max(ans, len(minHeap))
        return ans
        
        