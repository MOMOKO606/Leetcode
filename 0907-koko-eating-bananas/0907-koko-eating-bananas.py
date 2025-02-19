class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def eating_by(mid):
            return sum([ceil(num / mid) for num in piles])

        piles.sort()
        low, high = 1, piles[-1]
        while low <= high:
            mid = (low + high) // 2
            if eating_by(mid) > h:
                low = mid + 1
            else:
                high = mid - 1
        return low

        