class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def helper(num):
            ans = 0
            for pile in piles:
                ans += math.ceil(pile / num)
            return ans

        low, high = 1, max(piles)
        while low <= high:
            mid = (low + high) // 2
            if helper(mid) <= h: high = mid - 1
            else: low = mid + 1
        return low

        