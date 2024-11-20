class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points = sorted(points)
        curStart, curEnd, ans = points[0][0], points[0][1], 0
        for i in range(1, len(points) + 1):
            if i < len(points) and points[i][0] <= curEnd:
                curStart = max(curStart, points[i][0])
                curEnd = min(curEnd, points[i][1])
            else:
                ans += 1
                if i < len(points):
                    curStart, curEnd = points[i][0], points[i][1]               
        return ans
        