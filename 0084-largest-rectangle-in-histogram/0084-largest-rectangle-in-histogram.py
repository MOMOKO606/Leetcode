class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        ans, stack, heights = 0, [], [-inf] + heights + [-inf]
        for j, num in enumerate(heights):
            while stack and num < heights[stack[-1]]:
                k = stack.pop()
                ans = max(ans, (j - stack[-1] - 1) * heights[k])
            stack.append(j)
        return ans

        