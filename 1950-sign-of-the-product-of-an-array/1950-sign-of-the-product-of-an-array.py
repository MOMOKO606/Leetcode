class Solution:
    def arraySign(self, nums: List[int]) -> int:
        negative = 0
        for num in nums:
            if num == 0: return 0
            elif num < 0: negative += 1
        return 1 if not negative % 2 else -1

        
        