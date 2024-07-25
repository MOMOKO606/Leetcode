class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals)
        cur_start, cur_end, ans = intervals[0][0], intervals[0][1], []
        for i in range(1, len(intervals)):
            left, right = intervals[i][0], intervals[i][1]
            if cur_start <= left <= cur_end or cur_start <= right <= cur_end:
                cur_start, cur_end = min(cur_start, left), max(cur_end, right)
            else:
                ans.append([cur_start, cur_end])
                cur_start, cur_end = left, right
        return ans + [[cur_start, cur_end]]
        