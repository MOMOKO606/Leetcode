class Solution:
    def trap(self, height: List[int]) -> int:
        left, right, ans = [0] * len(height), [0] * len(height), 0
        for i in range(1, len(height)):
            left[i] = max(left[i - 1], height[i - 1])
        for j in range(len(height) - 2, -1, -1):
            right[j] = max(right[j + 1], height[j + 1])
        for i in range(1, len(height) - 1):
            ans += max(min(left[i], right[i]) - height[i], 0)
        return ans
        