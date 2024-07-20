class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        left, right, water = [-inf] * n, [-inf] * n, 0
        for i in range(1, n):
            left[i] = max(left[i - 1], height[i - 1])
        for j in range(n - 2, -1, -1):
            right[j] = max(right[j + 1], height[j + 1])
        for i in range(n):
            water += max(0, min(left[i], right[i]) - height[i])
        return water