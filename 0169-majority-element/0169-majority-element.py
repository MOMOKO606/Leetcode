class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        repeated, count = None, 0
        for num in nums:
            if not count: 
                repeated, count = num, 1
            elif num != repeated: count -= 1
            else: count += 1
        return repeated
        