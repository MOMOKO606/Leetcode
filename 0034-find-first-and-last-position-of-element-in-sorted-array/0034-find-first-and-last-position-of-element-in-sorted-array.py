class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def get_left():
            low, high = 0, len(nums) - 1
            while low <= high:
                mid = (low + high) // 2
                if target <= nums[mid]:
                    high = mid - 1
                else:
                    low = mid + 1
            return low

        def get_right():
            low, high = 0, len(nums) - 1
            while low <= high:
                mid = (low + high) // 2
                if target >= nums[mid]:
                    low = mid + 1
                else:
                    high = mid - 1
            return high
        
        if not nums: return [-1, -1]
        l, r = get_left(), get_right()
        return [l, r] if l < len(nums) and nums[l] == target else [-1, -1]

        

        