"""
# Definition for an Interval.
class Interval:
    def __init__(self, start: int = None, end: int = None):
        self.start = start
        self.end = end
"""

class Solution:
    def employeeFreeTime(self, schedule: '[[Interval]]') -> '[Interval]':
        intervals = []
        for employee in schedule:
            for interval in employee:
                intervals.append([interval.start, interval.end])
        intervals, ans = sorted(intervals), []
        cur_start, cur_end = intervals[0][0], intervals[0][1]
        for i in range(1, len(intervals)):
            if intervals[i][0] <= cur_end:
                cur_end = max(cur_end, intervals[i][1])
            else:
                ans.append(Interval(start=cur_end, end=intervals[i][0]))
                cur_start, cur_end = intervals[i][0], intervals[i][1]
        return ans


        