class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        if not intervals: return True
        intervals = sorted(intervals)
        cur_left, cur_right = intervals[0][0], intervals[0][1]
        for i in range(1, len(intervals)):
            if intervals[i][0] < cur_right: return False
            cur_left, cur_right = intervals[i][0], intervals[i][1]
        return True

        