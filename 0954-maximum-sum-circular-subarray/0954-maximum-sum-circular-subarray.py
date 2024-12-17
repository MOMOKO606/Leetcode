class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        largest, smallest, total1, total2, all_nagetive = 0, 0, 0, 0, True
        for num in nums:
            if num >= 0: all_nagetive = False

            if total1 + num < num: total1 = num
            else: total1 += num
            largest = max(largest, total1)

            if total2 + num > num: total2 = num
            else: total2 += num
            smallest = min(smallest, total2)

        return max(largest, sum(nums) - smallest) if not all_nagetive else max(nums)

        
        