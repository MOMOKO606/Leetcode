class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        i, window = 0, set([])
        for j, num in enumerate(nums):
            if j - i > k:
                window.remove(nums[i])
                i += 1
            if num in window: return True
            window.add(num)
        return False
        