class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort()
        cur_left, cur_right, ans = points[0][0], points[0][1], 0
        for i in range(1, len(points)):
            if points[i][0] <= cur_right:
                cur_left = max(cur_left, points[i][0])
                cur_right = min(cur_right, points[i][1])
            else:
                cur_left, cur_right, ans = points[i][0], points[i][1], ans + 1
        return ans + 1
        