class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], indexDiff: int, valueDiff: int) -> bool:
        largest, smallest, buckets = max(nums), min(nums), {}
        for j, num in enumerate(nums):
            if j > indexDiff:
                del buckets[(nums[j - indexDiff - 1] - smallest) // (valueDiff + 1)]
            k = (num - smallest) // (valueDiff + 1)
            if k in buckets: return True
            if k - 1 in buckets and num - buckets[k - 1] <= valueDiff: return True
            if k + 1 in buckets and buckets[k + 1] - num <= valueDiff: return True
            buckets[k] = num
        return False 


        