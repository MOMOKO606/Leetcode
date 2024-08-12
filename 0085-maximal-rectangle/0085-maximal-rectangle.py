class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        def getMaxRectangle(nums):
            nums, stack, area = [-inf] + nums + [-inf], [], -inf
            for j, num in enumerate(nums):
                while stack and num < nums[stack[-1]]:
                    k = stack.pop()
                    area = max(area, (j - stack[-1] - 1) * nums[k])
                stack.append(j)
            return area


        rows, cols, ans = len(matrix), len(matrix[0]), -inf
        nums = [0] * cols
        for i in range(rows):
            for j in range(cols):
                nums[j] = nums[j] + 1 if matrix[i][j] == "1" else 0
            ans = max(ans, getMaxRectangle(nums))
        return ans

        