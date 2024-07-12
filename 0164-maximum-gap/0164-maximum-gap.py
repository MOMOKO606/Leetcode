class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        largest, smallest = max(nums), min(nums)
        if largest == smallest: return 0
        interval  = math.ceil((largest - smallest) / (len(nums) - 1))
        buckets = [[None, None] for _ in range((largest - smallest) // interval + 1)]
        for num in nums:
            bucket = buckets[(num - smallest) // interval]
            bucket[0] = min(bucket[0], num) if bucket[0] else num
            bucket[1] = max(bucket[1], num) if bucket[1] else num
        buckets = [bucket for bucket in buckets if bucket[0]]
        return max(buckets[i][0] - buckets[i - 1][1] for i in range(1, len(buckets)) )
        