class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def cutArrayBy(mid):
            count, cur_total = 1, 0
            for num in nums:
                if cur_total + num <= mid:
                    cur_total += num
                else:
                    cur_total = num
                    count += 1
            return count


        low, high = max(nums), sum(nums)
        while low <= high:
            mid = (low + high) // 2
            if cutArrayBy(mid) <= k:
                high = mid - 1
            else:
                low = mid + 1
        return low
        
        