class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        @cache
        def helper(i, prev):
            if i == len(nums): return[]
            ans = []
            for j in range(i, len(nums)):
                if not nums[j] % prev:
                    ans = max(ans, [nums[j]] + helper(j + 1, nums[j]), key=len)
            return ans

        nums = sorted(nums)   
        return helper(0, 1)

        