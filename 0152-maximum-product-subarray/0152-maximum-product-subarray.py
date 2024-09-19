class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        smallest, largest, ans = nums[0], nums[0], nums[0]
        for num in nums[1:]:
            smallest, largest = min(num, smallest * num, largest * num), max(num, smallest * num, largest * num)
            ans = max(ans, largest)
        return ans
        