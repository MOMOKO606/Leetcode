class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        @cache
        def helper(i=0, prev=1):
            if i == len(nums): return []
            ans = helper(i + 1, prev)
            if not nums[i] % prev:
                ans = max(ans, [nums[i]] + helper(i + 1, nums[i]), key=len)
            return ans
        nums.sort()
        return helper()


        