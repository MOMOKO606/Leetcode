class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        def helper(mid):
            return sum([ceil(num / mid) for num in nums])

        low, high = 1, max(nums)
        while low <= high:
            mid = (low + high) // 2
            if helper(mid) <= threshold:
                high = mid - 1
            else:
                low = mid + 1
        return low

        