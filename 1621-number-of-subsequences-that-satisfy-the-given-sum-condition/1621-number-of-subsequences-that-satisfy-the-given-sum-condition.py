class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        nums, i, j, ans = sorted(nums), 0, len(nums) - 1, 0
        while i <= j:
            if nums[i] + nums[j] <= target:
                ans += 2 ** (j - i)
                i += 1
            else:
                j -= 1
        return ans % (10 ** 9 + 7)


        