class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        bisect.insort(intervals, newInterval)
        curStart, curEnd, ans = intervals[0][0], intervals[0][1], []
        for i in range(1, len(intervals)):
            if curStart <= intervals[i][0] <= curEnd:
                curStart, curEnd = min(curStart, intervals[i][0]), max(curEnd, intervals[i][1])
            else:
                ans.append([curStart, curEnd])
                curStart, curEnd = intervals[i][0], intervals[i][1]
        return ans + [[curStart, curEnd]]

        