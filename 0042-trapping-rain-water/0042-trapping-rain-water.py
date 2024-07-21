class Solution:
    def trap(self, height: List[int]) -> int:
        l, r, i, j, ans = height[0], height[-1], 1, len(height) - 2, 0
        while i <= j:
            if l <= r:
                ans += max(0, min(l, r) - height[i])
                l = max(l, height[i])
                i += 1
            else:
                ans += max(0, min(l, r) - height[j])
                r = max(r, height[j])
                j -= 1
        return ans

        