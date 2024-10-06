class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals)
        cur_start, cur_end, ans = intervals[0][0], intervals[0][1], []
        for i in range(1, len(intervals)):
            if intervals[i][0] <= cur_end:
                cur_end = max(cur_end, intervals[i][1])
            else:
                ans.append([cur_start, cur_end])
                cur_start, cur_end = intervals[i][0], intervals[i][1]
        return ans + [[cur_start, cur_end]]

        