class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums, ans = sorted(nums), inf
        for k in range(len(nums) - 2):
            i, j = k + 1, len(nums) - 1
            while i < j:
                pivot = nums[k] + nums[i] + nums[j]
                ans = min(ans, pivot, key=lambda x: abs(x - target))
                if pivot > target:
                    j -= 1
                else:
                    i += 1
        return ans

        