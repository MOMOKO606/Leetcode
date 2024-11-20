class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals = sorted(intervals)
        curEnd, ans = intervals[0][1], 0
        for i in range(1, len(intervals)):
            if intervals[i][0] >= curEnd: curEnd = intervals[i][1]
            else: ans, curEnd = ans + 1, min(curEnd, intervals[i][1])
        return ans

        