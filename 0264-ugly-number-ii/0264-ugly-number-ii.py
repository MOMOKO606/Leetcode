class Solution:
    def nthUglyNumber(self, n: int) -> int:
        p2, p3, p5, ans = 0, 0, 0, [1]
        for _ in range(n - 1):
            num2 = ans[p2] * 2
            num3 = ans[p3] * 3
            num5 = ans[p5] * 5
            ans.append(min(num2, num3, num5))
            if num2 == ans[-1]: p2 += 1
            if num3 == ans[-1]: p3 += 1
            if num5 == ans[-1]: p5 += 1
        return ans[-1]



        