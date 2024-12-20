class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        lis = []
        for num in nums:
            k = bisect.bisect_left(lis, num)
            if k == len(lis): lis.append(num)
            else: lis[k] = num
        return len(lis) > 2
        