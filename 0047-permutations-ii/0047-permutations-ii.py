class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        if not nums: return [[]]
        visited, ans = set(), []
        for i, num in enumerate(nums):
            if num in visited: continue
            visited.add(num)
            for seq in self.permuteUnique(nums[:i] + nums[i + 1:]):
                ans.append([nums[i]] + seq)
        return ans
        