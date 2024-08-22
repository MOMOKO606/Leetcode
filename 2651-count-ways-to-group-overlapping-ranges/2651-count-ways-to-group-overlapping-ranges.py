class Solution:
    def countWays(self, ranges: List[List[int]]) -> int:
        ranges = sorted(ranges)
        cur_start, cur_end, intervals = ranges[0][0], ranges[0][1], []
        for i in range(1, len(ranges)):
            if ranges[i][0] <= cur_end:
                cur_end = max(cur_end, ranges[i][1])
            else:
                intervals.append([cur_start, cur_end])
                cur_start, cur_end = ranges[i][0], ranges[i][1]
        return (2 ** (len(intervals) + 1)) % (10 ** 9 + 7)
    


        