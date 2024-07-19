class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def get_target_from_left(low=0, high=len(nums) - 1):
            while low <= high:
                mid = (low + high) // 2
                if target <= nums[mid]:
                    high = mid - 1
                else:
                    low = mid + 1
            return low if 0 <= low < len(nums) and nums[low] == target else -1

        def get_target_from_right(low=0, high=len(nums) - 1):
            while low <= high:
                mid = (low + high) // 2
                if target < nums[mid]:
                    high = mid - 1
                else:
                    low = mid + 1
            return high if 0 <= high < len(nums) and nums[high] == target else -1

        return [get_target_from_left(), get_target_from_right()]


        