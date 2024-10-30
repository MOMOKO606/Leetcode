class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        heights, ans, stack = [-inf] + heights + [-inf], 0, []
        for j, height in enumerate(heights):
            while stack and heights[stack[-1]] > height:
                k = stack.pop()
                i = stack[-1]
                ans = max(ans, heights[k] * (j - i - 1))
            stack.append(j)
        return ans

        