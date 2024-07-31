class Solution:
    def mySqrt(self, x: int) -> int:
        low, high = 1, x
        while low <= high:
            mid = (low + high) // 2
            pivot = mid * mid
            if pivot == x: return mid
            elif pivot < x: low = mid + 1
            else: high = mid - 1
        return high
        