class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[List[int]]:
        if not nums: return [[lower, upper]]
        ans, i = [], 0
        if nums[0] > lower: ans.append([lower, nums[0] - 1])
        for j in range(len(nums)):
            if j > 0 and nums[j] - nums[j - 1] > 1:
                ans.append([nums[j - 1] + 1, nums[j] - 1])
        if nums[-1] < upper: ans.append([nums[-1] + 1, upper])
        return ans
        