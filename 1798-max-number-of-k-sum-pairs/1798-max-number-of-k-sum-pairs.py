class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums, i, j, ans = sorted(nums), 0, len(nums) - 1, 0
        while i < j:
            pivot = nums[i] + nums[j]
            if pivot == k:
                ans, i, j = ans + 1, i + 1, j - 1
            elif pivot < k:
                i += 1
            else:
                j -= 1
        return ans

        