class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        rows, cols, ans = len(nums1), len(nums2), 0
        dp = [[0] * (cols + 1) for _ in range(rows + 1)]
        for i in range(1, rows + 1):
            for j in range(1, cols + 1):
                if nums1[i - 1] == nums2[j - 1]:
                    dp[i][j] = 1 + dp[i - 1][j - 1]
                    ans = max(ans, dp[i][j])
        return ans
        