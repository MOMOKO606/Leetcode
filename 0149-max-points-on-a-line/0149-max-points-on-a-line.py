class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        if len(points) == 1: return 1
        ans = 1
        for first_point in points:
            slopes = {}
            for second_point in points:
                if second_point == first_point: continue
                slope = (second_point[1] - first_point[1]) / (second_point[0] - first_point[0]) if second_point[0] != first_point[0] else inf
                slopes[slope] = slopes.get(slope, 0) + 1
                ans = max(ans, slopes[slope])
        return ans + 1
        