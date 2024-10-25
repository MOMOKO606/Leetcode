class Solution:
    def trap(self, height: List[int]) -> int:
        left_max, right_max, ans = [0] * len(height), [0] * len(height), 0
        for i in range(1, len(height)):
            left_max[i] = max(left_max[i - 1], height[i - 1])
        for j in range(len(height) - 2, -1, -1):
            right_max[j] = max(right_max[j + 1], height[j + 1])
        for i in range(1, len(height) - 1):
            ans += max(min(left_max[i], right_max[i]) - height[i], 0)
        return ans
        