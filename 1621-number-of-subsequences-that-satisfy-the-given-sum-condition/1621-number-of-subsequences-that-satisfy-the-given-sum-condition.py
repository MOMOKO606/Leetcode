class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        ans, j, nums = 0, len(nums) - 1, sorted(nums)
        for i, num in enumerate(nums):
            while i <= j and nums[i] + nums[j] > target:
                j -= 1
            ans += 2 ** (j - i) if i <= j else 0
        return ans % (10 ** 9 + 7)


            



        