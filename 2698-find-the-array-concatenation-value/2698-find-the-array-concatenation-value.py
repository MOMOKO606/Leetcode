class Solution:
    def findTheArrayConcVal(self, nums: List[int]) -> int:
        i, j, ans = 0, len(nums) - 1, 0
        while i < j:
            ans += int(str(nums[i]) + str(nums[j]))
            i, j = i + 1, j - 1
        if i == j: ans += nums[i]
        return ans
        