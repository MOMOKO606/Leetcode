class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if not nums: return [[]]
        return [[nums[i]] + seq for i in range(len(nums)) for seq in self.permute(nums[:i] + nums[i + 1:])]