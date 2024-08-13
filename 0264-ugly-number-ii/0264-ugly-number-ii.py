class Solution:
    def nthUglyNumber(self, n: int) -> int:
        p2, p3, p5, factors = 0, 0, 0, [1]
        for _ in range(n - 1):
            p2_num = 2 * factors[p2]
            p3_num = 3 * factors[p3]
            p5_num = 5 * factors[p5]
            key = min(p2_num, p3_num, p5_num)
            factors.append(key)
            if key == p2_num: p2 += 1
            if key == p3_num: p3 += 1
            if key == p5_num: p5 += 1
        return factors[-1]

        