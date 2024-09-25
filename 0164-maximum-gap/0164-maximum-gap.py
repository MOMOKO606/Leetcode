class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        max_num, min_num = max(nums), min(nums)
        if max_num == min_num: return 0
        l = math.ceil((max_num - min_num) / (len(nums) - 1))
        intervals = [[None, None] for _ in range((max_num - min_num) // l + 1)]
        for num in nums:
            interval = intervals[(num - min_num) // l]
            interval[0] = min(interval[0], num) if interval[0] else num
            interval[1] = max(interval[1], num) if interval[1] else num
        intervals = [interval for interval in intervals if interval[0]]
        return max([intervals[i][0] - intervals[i - 1][1] for i in range(1, len(intervals))])

        