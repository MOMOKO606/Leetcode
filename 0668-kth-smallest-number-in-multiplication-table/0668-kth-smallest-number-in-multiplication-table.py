class Solution:
    def findKthNumber(self, m: int, n: int, k: int) -> int:
        def lessOrEqual(mid):
            ans = 0
            for i in range(1, n + 1):
                ans += min(m, mid // i)
            return ans


        low, high = 1, m * n
        while low <= high:
            mid = (low + high) // 2
            if lessOrEqual(mid) >= k:
                high = mid - 1
            else:
                low = mid + 1
        return low

        