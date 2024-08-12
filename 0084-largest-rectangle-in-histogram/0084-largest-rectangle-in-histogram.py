class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        heights, stack, ans = [-inf] + heights + [-inf], [], -inf
        for j, height in enumerate(heights):
            while stack and height < heights[stack[-1]]:
                k = stack.pop()
                ans = max(ans, (j - stack[-1] - 1) * heights[k])
            stack.append(j)
        return ans

        