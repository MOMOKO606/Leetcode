class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n, stack = len(nums), []
        nums += nums
        ans = [-1] * len(nums)
        for i, num in enumerate(nums):
            while stack and num > nums[stack[-1]]:
                j = stack.pop()
                ans[j] = num
            stack.append(i)
        return ans[:n]

        