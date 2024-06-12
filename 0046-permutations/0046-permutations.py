class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def helper(nums, seq):
            if not nums: 
                self.ans.append(seq[:])
                return 
            for i in range(len(nums)):
                helper(nums[:i] + nums[i + 1:], seq + [nums[i]])

        self.ans = []
        helper(nums, [])
        return self.ans
