class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        @cache
        def helper(prev=1, i=0):
            if i == len(nums): return []
            ans = []
            for j in range(i, len(nums)):
                if not nums[j] % prev:
                    ans = max(ans, [nums[j]] + helper(nums[j], j + 1), key=len)
            return ans

        nums = sorted(nums)
        return helper()
        