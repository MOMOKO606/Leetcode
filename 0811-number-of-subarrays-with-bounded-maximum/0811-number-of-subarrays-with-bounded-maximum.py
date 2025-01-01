class Solution:
    def numSubarrayBoundedMax(self, nums: List[int], left: int, right: int) -> int:
        nums, stack, ans = [inf] + nums + [inf], [], 0
        for j, num in enumerate(nums):
            while stack and nums[stack[-1]] < num:
                k = stack.pop()
                if left <= nums[k] <= right:
                    ans += (j - k) * (k - stack[-1])
            stack.append(j)
        return ans
        