class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        largest, smallest, ans = 1, 1, -inf
        for num in nums:
           largest, smallest = max(largest * num, smallest * num, num), min(largest * num, smallest * num, num)
           ans = max(ans, largest)
        return ans