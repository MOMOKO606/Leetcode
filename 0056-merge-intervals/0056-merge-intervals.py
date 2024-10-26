class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals)
        cur_left, cur_right, ans = intervals[0][0], intervals[0][1], []
        for j in range(1, len(intervals)):
            if intervals[j][0] <= cur_right:
                cur_right = max(cur_right, intervals[j][1])
            else:
                ans.append([cur_left, cur_right])
                cur_left, cur_right = intervals[j][0], intervals[j][1]
        return ans + [[cur_left, cur_right]]
        