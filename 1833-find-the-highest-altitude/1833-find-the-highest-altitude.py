class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        ans, altitude = 0, 0
        for num in gain:
            altitude += num
            ans = max(ans, altitude)
        return ans
        