class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        def helper(pos=0, n=4, target=target, seq=[]):
            if n == 2: 
                i, j = pos, len(nums) - 1
                while i < j:
                    key = nums[i] + nums[j]
                    if key == target:
                        self.ans.append(seq + [nums[i], nums[j]])
                        i += 1
                        while i < len(nums) and nums[i] == nums[i - 1]:
                            i += 1
                        j -= 1
                        while j >= 0 and nums[j] == nums[j + 1]:
                            j -= 1 
                    elif key < target:
                        i += 1
                    else:
                        j -= 1
                return 
            for k in range(pos, len(nums) - n + 1):
                if k > pos and nums[k] == nums[k - 1]: continue
                helper(k + 1, n - 1, target - nums[k], seq + [nums[k]])
        
        self.ans, nums = [], sorted(nums)
        helper()
        return self.ans

        