class Solution:
    def trap(self, height: List[int]) -> int:
        left, right, i, j, ans = height[0], height[-1], 1, len(height) - 2, 0
        while i <= j:
            if left <= right:
                ans += max(left - height[i], 0)
                i, left = i + 1, max(left, height[i])
            else:
                ans += max(right - height[j], 0)
                j, right = j - 1, max(right, height[j])
        return ans

        