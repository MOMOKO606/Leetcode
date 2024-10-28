class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2: return x
        left, right = 1, x
        while left <= right:
            mid = (left + right) // 2
            pivot = mid * mid
            if pivot == x: return mid
            if pivot > x:
                right = mid - 1
            else:
                left = mid + 1
        return right
        