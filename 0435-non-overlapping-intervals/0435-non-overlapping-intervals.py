class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals = sorted(intervals)
        cur_left, cur_right, ans = intervals[0][0], intervals[0][1], 0
        for i in range(1, len(intervals)):
            l, r = intervals[i][0], intervals[i][1]
            if l < cur_right:
                cur_right, ans = min(cur_right, r), ans + 1
            else:
                cur_left, cur_right = l, r
        return ans 
        