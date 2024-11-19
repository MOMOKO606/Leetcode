class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def split(mid):
            count, total = 1, 0
            for num in nums:
                if total + num > mid:
                    count, total = count + 1, num
                else:
                    total += num
            return count



        low, high = max(nums), sum(nums)
        while low <= high:
            mid = (low + high) // 2
            if split(mid) <= k:
                high = mid - 1
            else:
                low = mid + 1
        return low

        