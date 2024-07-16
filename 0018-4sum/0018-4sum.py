class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        def helper(start, n, target, seq):
            if n == 2:
                l, r = start, len(nums) - 1
                while l < r:
                    key = nums[l] + nums[r]
                    if key == target:
                        ans.append(seq + [nums[l], nums[r]])
                        l += 1
                        while l < len(nums) and nums[l] == nums[l - 1]:
                            l += 1
                        r -= 1
                        while r >= 0 and nums[r] == nums[r + 1]:
                            r -= 1
                    elif key < target: l += 1
                    else: r -= 1
                return 
            for k in range(start, len(nums) - n + 1):
                if k > start and nums[k] == nums[k - 1]: continue
                helper(k + 1, n - 1, target - nums[k], seq + [nums[k]])
        
        ans, nums = [], sorted(nums)
        helper(0, 4, target, [])
        return ans
        