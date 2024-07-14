class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], indexDiff: int, valueDiff: int) -> bool:
        buckets = {}
        for i, num in enumerate(nums):
            if i > indexDiff: 
                j = nums[i - indexDiff - 1] // (valueDiff + 1)
                del buckets[j]
            k = nums[i] // (valueDiff + 1)
            if k in buckets: return True
            if k - 1 in buckets and abs(num - buckets[k - 1]) <= valueDiff: return True 
            if k + 1 in buckets and abs(num - buckets[k + 1]) <= valueDiff: return True 
            buckets[k] = num
        return False



        