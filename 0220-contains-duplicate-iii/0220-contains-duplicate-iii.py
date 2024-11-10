class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], indexDiff: int, valueDiff: int) -> bool:
        buckets, smallest, largest = {}, min(nums), max(nums)
        for j, num in enumerate(nums):
            if j > indexDiff:
                i = j - indexDiff - 1
                del buckets[(nums[i] - smallest) // (valueDiff + 1)]
            k = (num - smallest) // (valueDiff + 1)
            if k in buckets: return True
            if k - 1 in buckets and abs(num - buckets[k - 1]) <= valueDiff: return True
            if k + 1 in buckets and abs(num - buckets[k + 1]) <= valueDiff: return True
            buckets[k] = num
        return False

        