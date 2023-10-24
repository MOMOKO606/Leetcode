class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals, ans, maxEnd = sorted(intervals, key = lambda x: x[1]), 0, -math.inf
        for start, end in intervals:
            if start >= maxEnd: maxEnd = end
            else:
                ans += 1
                maxEnd = min(maxEnd, end)
        return ans
        