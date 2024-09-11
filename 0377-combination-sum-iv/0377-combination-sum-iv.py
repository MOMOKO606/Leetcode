class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        @cache
        def helper(target):
            if target < 0: return 0
            if not target: return 1
            ans = 0
            for num in nums:
                ans += helper(target - num)
            return ans
        
        return helper(target)
        