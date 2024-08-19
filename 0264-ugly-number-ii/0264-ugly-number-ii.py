class Solution:
    def nthUglyNumber(self, n: int) -> int:
        p2, p3, p5, ans = 0, 0, 0, [1]
        for _ in range(n - 1):
            num2 = 2 * ans[p2]
            num3 = 3 * ans[p3]
            num5 = 5 * ans[p5]
            key = min(num2, num3, num5)
            ans.append(key)
            if key == num2: p2 += 1
            if key == num3: p3 += 1
            if key == num5: p5 += 1
        return ans[-1]
        