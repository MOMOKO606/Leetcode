class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        def helper(n, start, target, seq):
            if n < 3:
                i, j = start, len(nums) - 1
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
            for i in range(start, len(nums)):
                if i > start and nums[i] == nums[i - 1]: continue
                helper(n - 1, i + 1, target - nums[i], seq + [nums[i]])

        nums, self.ans = sorted(nums), []
        helper(4, 0, target, [])
        return self.ans