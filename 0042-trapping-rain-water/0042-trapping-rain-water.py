class Solution:
    def trap(self, height: List[int]) -> int:
        left_max, right_max, i, j, ans = height[0], height[-1], 1, len(height) - 2, 0
        while i <= j:
            if left_max <= right_max:
                ans += max(0, left_max - height[i])
                left_max = max(left_max, height[i])
                i += 1
            else:
                ans += max(0, right_max - height[j])
                right_max = max(right_max, height[j])
                j -= 1
        return ans



        