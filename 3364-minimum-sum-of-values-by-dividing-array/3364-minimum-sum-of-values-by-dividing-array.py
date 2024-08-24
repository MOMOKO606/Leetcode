class Solution:
    def minimumValueSum(self, nums: List[int], andValues: List[int]) -> int:
        @cache
        def helper(i, j, _AND):
            if i == len(nums) and j == len(andValues): return 0
            if i == len(nums) or j == len(andValues): return inf
            _AND &= nums[i]
            if _AND < andValues[j]: return inf
            ans = helper(i + 1, j, _AND)
            if _AND == andValues[j]:
                ans = min(ans, nums[i] + helper(i + 1, j + 1, -1))
            return ans
        ans = helper(0, 0, -1)
        return ans if ans != inf else -1



        