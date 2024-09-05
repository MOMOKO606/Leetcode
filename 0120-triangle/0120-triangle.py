class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        for i in range(1, len(triangle)):
            triangle[i][0] += triangle[i - 1][0]

        for i in range(1, len(triangle)):
            for j in range(1, len(triangle[i])):
                triangle[i][j] = triangle[i][j] + min(triangle[i - 1][j], triangle[i - 1][j - 1]) if j < len(triangle[i - 1]) else  triangle[i][j] + triangle[i - 1][j - 1]

        return min(triangle[-1])


    
        