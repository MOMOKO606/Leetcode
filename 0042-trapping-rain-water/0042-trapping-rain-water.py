class Solution:
    def trap(self, height: List[int]) -> int:
        stack, ans = [], 0
        for j, num in enumerate(height):
            while stack and num >= height[stack[-1]]:
                k = stack.pop()
                if stack:
                    i = stack[-1]
                    ans += max(0, min(height[j], height[i]) - height[k]) * (j - i - 1)
            stack.append(j)
        return ans


        