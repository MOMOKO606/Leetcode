class Solution:
    def nthUglyNumber(self, n: int) -> int:
        ans, p2, p3, p5 = [1], 0, 0, 0
        while n - 1:
            num2, num3, num5 = ans[p2] * 2, ans[p3] * 3, ans[p5] * 5
            pivot = min(num2, num3, num5)
            if pivot == num2:
                p2 += 1
            if pivot == num3:
                p3 += 1
            if pivot == num5:
                p5 += 1
            ans.append(pivot)
            n -= 1
        return ans[-1]

        