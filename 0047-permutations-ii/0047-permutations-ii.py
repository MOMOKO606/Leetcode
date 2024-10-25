class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        if not nums: return [[]]
        visited, ans = set(), []
        for i in range(len(nums)):
            if nums[i] in visited: continue
            visited.add(nums[i])
            ans += [[nums[i]] + seq for seq in self.permuteUnique(nums[:i] + nums[i + 1:])]
        return ans


        