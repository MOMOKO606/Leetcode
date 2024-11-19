class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        deltas = [nums[i] - nums[i - 1] for i in range(1, len(nums))]
        i, ans = 0, 0
        for j in range(len(deltas) + 1):
            if j == len(deltas) or deltas[j] != deltas[i]:
                n = j - i
                ans += n * (n - 1) // 2
                i = j
        return ans


        