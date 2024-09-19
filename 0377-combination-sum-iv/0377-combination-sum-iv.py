class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        @cache
        def helper(target=target):
            if not target: return 1
            if target < 0: return 0
            return sum(helper(target - num) for num in nums)

        return helper()
        