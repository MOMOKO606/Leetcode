class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums, ans, i, j = sorted(nums), 0, 0, len(nums) - 1
        while i < j:
            if nums[i] + nums[j] == k: ans, i, j = ans + 1, i + 1, j - 1
            elif nums[i] + nums[j] < k: i += 1
            else: j -= 1
        return ans

        