class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        mode, count = None, 0
        for num in nums:
            if not mode: 
                mode, count = num, 1
            elif num != mode:
                count -= 1
                if not count: mode = None
            else:
                count += 1
        return mode
        