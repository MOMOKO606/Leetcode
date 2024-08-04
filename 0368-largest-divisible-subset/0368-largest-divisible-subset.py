class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        @cache
        def dfs(i, prev):
            if i == len(nums): return []
            res = dfs(i + 1, prev)
            if nums[i] % prev == 0:
                tmp = [nums[i]] + dfs(i + 1, nums[i])
                res = tmp if len(tmp) > len(res) else res
            return res 
        nums.sort()
        return dfs(0, 1)