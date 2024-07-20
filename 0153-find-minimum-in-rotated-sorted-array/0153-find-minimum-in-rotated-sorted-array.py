class Solution:
    def findMin(self, nums: List[int]) -> int:
        low, high = 0, len(nums) - 1
        while low < high:
            mid = (low + high) // 2
            if nums[low] <= nums[mid] < nums[high] or nums[mid] < nums[high] < nums[low]:
                high = mid
            else:
                low = mid + 1
        return nums[low]
        