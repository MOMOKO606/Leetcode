class Solution:
    def trap(self, height: List[int]) -> int:
        l, r, i, j, ans = height[0], height[-1], 1, len(height) - 2, 0
        while i <= j:
            if l <= r:
                ans, l, i = ans + max(l - height[i], 0), max(l, height[i]), i + 1
            else:
                ans, r, j = ans + max(r - height[j], 0), max(r, height[j]), j - 1
        return ans


        