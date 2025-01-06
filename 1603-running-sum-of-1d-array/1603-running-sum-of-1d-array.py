class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        preSum, ans = 0, []
        for num in nums:
            preSum += num
            ans.append(preSum)
        return ans
        