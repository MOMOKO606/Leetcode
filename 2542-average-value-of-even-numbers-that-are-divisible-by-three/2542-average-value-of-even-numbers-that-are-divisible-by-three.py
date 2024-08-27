class Solution:
    def averageValue(self, nums: List[int]) -> int:
        total, count = 0, 0
        for num in nums:
            if not num & 1 and not num % 3: total, count = total + num, count + 1
        return total // count if count else 0
        