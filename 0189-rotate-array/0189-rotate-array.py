class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def reverseNums(i, j):
            while i < j:
                nums[i], nums[j] = nums[j], nums[i]
                i, j = i + 1, j - 1
        k %= len(nums)
        reverseNums(0, len(nums) - 1)
        reverseNums(0, k - 1)
        reverseNums(k, len(nums) - 1)
        