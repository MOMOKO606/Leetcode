class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        rows, cols = len(nums1) + 1, len(nums2) + 1
        dp, ans = [[0] * cols for _ in range(rows)], 0
        for i in range(1, rows):
            for j in range(1, cols):
                if nums1[i - 1] == nums2[j - 1]: 
                    dp[i][j] = dp[i - 1][j - 1] + 1
                    ans = max(ans, dp[i][j])
        return ans
        
        