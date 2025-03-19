class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        cur_left, cur_right, ans = intervals[0][0], intervals[0][1], 0
        for i in range(1, len(intervals)):
            if intervals[i][0] < cur_right:
                cur_right, ans = min(cur_right, intervals[i][1]), ans + 1
            else:
                cur_left, cur_right = intervals[i][0], intervals[i][1]
        return ans

        