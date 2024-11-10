class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        mode1, mode2, count1, count2 = None, None, 0, 0
        for num in nums:
            if num == mode1: count1 += 1
            elif num == mode2: count2 += 1
            elif mode1 is None: mode1, count1 = num, 1
            elif mode2 is None: mode2, count2 = num, 1
            else:
                count1, count2 = count1 - 1, count2 - 1
                if not count1: mode1 = None
                if not count2: mode2 = None
        return [mode for mode in [mode1, mode2] if nums.count(mode) > len(nums) // 3]
        