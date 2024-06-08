class Solution:
    def trap(self, height: List[int]) -> int:
        left, right, ans = [0] * len(height), [0] * len(height), 0
        for i in range(1, len(height)):
            left[i] = max(height[i - 1], left[i - 1])
        for i in range(len(height) - 2, -1, -1):
            right[i] = max(height[i + 1], right[i + 1])
        for i in range(1, len(height) - 1):
            ans += max(0, min(left[i], right[i]) - height[i])
        return ans


        