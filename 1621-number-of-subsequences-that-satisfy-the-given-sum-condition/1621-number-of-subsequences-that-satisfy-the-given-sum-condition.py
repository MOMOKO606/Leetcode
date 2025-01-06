class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        ans, nums, j = 0, sorted(nums), len(nums) - 1
        for i, num in enumerate(nums):
            while i <= j and num + nums[j] > target:
                j -= 1
            ans += 2 ** (j - i) if i <= j else 0
        return ans % (10 ** 9 + 7)
