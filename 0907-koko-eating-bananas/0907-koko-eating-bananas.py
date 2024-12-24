class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def get_k(mid):
            return sum([ceil(pile / mid) for pile in piles])
        
        
        low, high = 1, max(piles)
        while low <= high:
            mid = (low + high) // 2
            if get_k(mid) <= h:
                high = mid - 1
            else:
                low = mid + 1
        return low
        