class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        cur, ans = 0, 0
        for num in gain:
            cur += num
            ans = max(ans, cur)
        return ans
        