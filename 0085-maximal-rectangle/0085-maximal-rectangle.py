class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        def get_max_area(nums):
            nums, stack, ans = [-inf] + nums + [-inf], [], 0
            for j, num in enumerate(nums):
                while stack and nums[stack[-1]] > num:
                    ans = max(ans, nums[stack.pop()] * (j - stack[-1] - 1))
                stack.append(j)
            return ans


        rows, cols, ans = len(matrix), len(matrix[0]), 0
        for i in range(rows):
            for j in range(cols):
                matrix[i][j] = int(matrix[i][j])
                if i > 0: 
                    matrix[i][j] = matrix[i][j] + matrix[i - 1][j] if matrix[i][j] else 0
            ans = max(ans, get_max_area(matrix[i][:]))
        return ans
               


        