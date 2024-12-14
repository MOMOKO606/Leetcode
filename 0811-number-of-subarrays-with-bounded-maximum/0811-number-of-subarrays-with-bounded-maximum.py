class Solution:
    def numSubarrayBoundedMax(self, nums: List[int], left: int, right: int) -> int:
        ans, stack, nums = 0, [], [inf] + nums + [inf]
        for j, num in enumerate(nums):
            while stack and num > nums[stack[-1]]:
                k = stack.pop()
                if left <= nums[k] <= right:
                    ans += (k - stack[-1]) * (j - k)
            stack.append(j)
        return ans
        