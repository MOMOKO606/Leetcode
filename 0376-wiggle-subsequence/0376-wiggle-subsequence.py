class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        ans = [nums[0]]
        for i in range(1, len(nums)):
            if len(ans) > 1 and (nums[i] - ans[-1]) * (ans[-1] - ans[-2]) >= 0:
                ans[-1] = nums[i] 
            elif nums[i] != ans[-1]: 
                ans.append(nums[i])
        return len(ans)
        