class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        def helper(nums):
            if not nums: return [[]]
            ans = []
            for i in range(len(nums)):
                if i > 0 and nums[i] == nums[i - 1]: continue
                ans += [[nums[i]] + seq for seq in helper(nums[:i] + nums[i + 1:])]
            return ans
        nums = sorted(nums)
        return helper(nums)
        