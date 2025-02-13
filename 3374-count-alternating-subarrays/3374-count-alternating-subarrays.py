class Solution:
    def countAlternatingSubarrays(self, nums: List[int]) -> int:
        ans, i = 0, -1
        for j in range(len(nums)):
            if j > 0 and nums[j] == nums[j - 1]:
                i = j - 1
            ans += j - i
        return ans
        