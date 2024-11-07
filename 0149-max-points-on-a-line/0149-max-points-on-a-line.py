class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        ans = 0
        for point1 in points:
            slopes = {}
            for point2 in points:
                if point2 == point1: continue
                slope = (point2[1] - point1[1]) / (point2[0] - point1[0]) if point2[0] != point1[0] else inf
                slopes[slope] = slopes.get(slope, 0) + 1
                ans = max(ans, slopes[slope])
        return ans + 1
        